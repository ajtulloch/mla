from sklearn import metrics, cross_validation
import numpy as np
from scipy import interp
from gen.protobufs.ml_pb2 import Model, TrainingReport


def roc_curve(clf, X, y, n_folds=5):
    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 101)

    for train, test in cross_validation.StratifiedKFold(y, n_folds=n_folds):
        probas = clf.fit(X[train], y[train]).predict_proba(X[test])
        # Compute ROC curve and area the curve
        fpr, tpr, thresholds = metrics.roc_curve(y[test], probas[:, 1])
        mean_tpr += interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0
    mean_tpr /= n_folds
    return [Model.PerformanceStatistics.ROCPoint(
        falsePositiveRate=fpr,
        truePositiveRate=tpr) for (fpr, tpr) in zip(mean_fpr, mean_tpr)]


def simple_builder(clf):
    def run(X, y):
        return (clf.fit(X, y), Model.Parameters(), Model.FeatureImportances())
    return run


def summary_statistics(X, y):
    return TrainingReport.SummaryStatistics(
        numExamples=len(y), numPositives=len(y[y > 0]))
