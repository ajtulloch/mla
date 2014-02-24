from sklearn import linear_model
from gen.protobufs.ml_pb2 import TrainingReport, Model
from sklearn import cross_validation
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

def summary_statistics(X, y):
    return TrainingReport.SummaryStatistics(
        numExamples=len(y), numPositives=len(y[y > 0]))


def performance_statistics(clf, X, y):
    statistics = Model.PerformanceStatistics(metrics=[])
    for pb_metric, sklearn_metric_string in PB_METRICS.iteritems():
        try:
            statistics.metrics.append(Model.PerformanceStatistics.Performance(
                metric=pb_metric,
                score=cross_validation.cross_val_score(
                    clf, X, y, scoring=sklearn_metric_string)))
        except:
            log.exception("Exception computing metric: %s",
                          (pb_metric, sklearn_metric_string))
    return statistics


def serialized(clf):
    return Model.Serialized(pickledStrings=cPickle.dumps(clf))


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

    @staticmethod
    def build(online_train_requests):
        return
