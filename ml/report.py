from sklearn import linear_model, ensemble, cross_validation
from gen.protobufs.ml_pb2 import TrainingReport, Model
import cPickle

import numpy as np
import logging

log = logging.getLogger(__name__)

METRICS = ['accuracy', 'average_precision', 'f1',
           'log_loss', 'precision', 'recall', 'roc_auc']

PB_METRICS = {
    Model.PerformanceStatistics.ACCURACY: 'accuracy',
    Model.PerformanceStatistics.AVERAGE_PRECISION: 'average_precision',
    Model.PerformanceStatistics.F1: 'f1',
    Model.PerformanceStatistics.LOG_LOSS: 'log_loss',
    Model.PerformanceStatistics.PRECISION: 'precision',
    Model.PerformanceStatistics.RECALL: 'recall',
    Model.PerformanceStatistics.ROC_AUC: 'roc_auc',
}

MODEL_BUILDERS = {
    Model.LOGISTIC_REGRESSION:
    lambda X, y: (linear_model.LogisticRegression().fit(X, y),
                  Model.Parameters(),
                  Model.FeatureImportances()),
    Model.GRADIENT_BOOSTED:
    lambda X, y: (ensemble.GradientBoostingClassifier().fit(X, y),
                  Model.Parameters(),
                  Model.FeatureImportances()),
}


def summary_statistics(X, y):
    return TrainingReport.SummaryStatistics(
        numExamples=len(y), numPositives=len(y[y > 0]))


def performance_statistics(clf, X, y):
    def performance(metric):
        folds = \
            cross_validation.cross_val_score(clf, X, y,
                                             scoring=PB_METRICS[metric])
        return Model.PerformanceStatistics.Performance(
            metric=metric, score=np.mean(folds))
    metrics = [performance(metric) for metric in PB_METRICS.iterkeys()]
    return Model.PerformanceStatistics(metrics=metrics)


def serialized(clf):
    return Model.Serialized(pickledString=cPickle.dumps(clf))


def build_model(algorithm, fit_function):
    def run(X, y):
        clf, parameters, featureImportances = fit_function(X, y)
        return Model(
            algorithm=algorithm,
            parameters=parameters,
            performanceStatistics=performance_statistics(clf, X, y),
            featureImportances=featureImportances,
            serialized=serialized(clf))
    return run


# TODO(tulloch) - remove this
class Reporter(object):
    @staticmethod
    def report(online_train_requests):
        results = {}
        X = np.array([list(r.features) for r in online_train_requests])
        y = np.array([r.label for r in online_train_requests])
        log.info("X: %s, y: %s", X, y)
        for metric in METRICS:
            log.info("Computing metric: %s", metric)
            scores = cross_validation.cross_val_score(
                linear_model.LogisticRegression(), X, y, scoring=metric)
            results[metric] = np.mean(scores)
            log.info("Metric: %s", scores)
        return results


class ProtobufReporter(object):
    @staticmethod
    def build(online_train_requests):
        X = np.array([list(r.features) for r in online_train_requests])
        y = np.array([r.label for r in online_train_requests])

        models = [build_model(algorithm, fit_function)(X, y)
                  for algorithm, fit_function in MODEL_BUILDERS.iteritems()]
        return TrainingReport(
            summaryStatistics=summary_statistics(X, y),
            models=models)
