from sklearn import linear_model, ensemble, svm, cross_validation

from gen.protobufs.ml_pb2 import TrainingReport, Model
from performance import roc_curve, simple_builder, summary_statistics
import numpy as np
import logging

log = logging.getLogger(__name__)

METRICS = {
    Model.PerformanceStatistics.ACCURACY: 'accuracy',
    Model.PerformanceStatistics.AVERAGE_PRECISION: 'average_precision',
    Model.PerformanceStatistics.F1: 'f1',
    Model.PerformanceStatistics.LOG_LOSS: 'log_loss',
    Model.PerformanceStatistics.PRECISION: 'precision',
    Model.PerformanceStatistics.RECALL: 'recall',
    Model.PerformanceStatistics.ROC_AUC: 'roc_auc',
}

MODEL_BUILDERS = {
    Model.LOGISTIC_REGRESSION: simple_builder(
        linear_model.LogisticRegression()),
    # Model.GRADIENT_BOOSTED: simple_builder(
    #     ensemble.GradientBoostingClassifier(n_estimators=20)),
    Model.RANDOM_FORESTS: simple_builder(
        ensemble.RandomForestClassifier()),
    Model.LINEAR_SVM: simple_builder(
        svm.SVC(kernel='linear', probability=True)),
    Model.NONLINEAR_SVM: simple_builder(
        svm.SVC(kernel='rbf', probability=True)),
}


def performance_statistics(clf, X, y):
    def cv_performance(metric):
        folds = cross_validation.cross_val_score(
            clf, X, y, scoring=METRICS[metric], n_jobs=-1)

        return Model.PerformanceStatistics.Performance(
            metric=metric, score=np.mean(folds))
    metrics = [cv_performance(metric) for metric in METRICS.iterkeys()]
    return Model.PerformanceStatistics(
        metrics=metrics,
        rocCurve=roc_curve(clf, X, y))


def serialized(clf):
    # pickledString = cPickle.dumps(clf)
    # pickled unused while we figure out persistence strategy.
    return Model.Serialized()


def build_model(algorithm, fit_function):
    def run(X, y):
        log.info("Running algorithm: %s", algorithm)
        clf, parameters, featureImportances = fit_function(X, y)
        return Model(
            algorithm=algorithm,
            parameters=parameters,
            performanceStatistics=performance_statistics(clf, X, y),
            featureImportances=featureImportances,
            serialized=serialized(clf))
    return run


class ProtobufReporter(object):
    @staticmethod
    def build(online_train_requests):
        log.info("Starting training on %s examples",
                 len(online_train_requests))

        X = np.array([np.array(r.features) for r in online_train_requests])
        y = np.array([r.label for r in online_train_requests])

        models = [build_model(algorithm, fit_function)(X, y)
                  for algorithm, fit_function in MODEL_BUILDERS.iteritems()]
        log.info("Trained %s models", len(models))

        return TrainingReport(
            summaryStatistics=summary_statistics(X, y),
            models=models)
