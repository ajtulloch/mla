from sklearn import metrics
from sklearn.cross_validation import StratifiedKFold
import numpy as np
from scipy import interp
from gen.protobufs.ml_pb2 import Model


def roc_curve(clf, X, y, n_folds=5):
    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 101)

    for train, test in StratifiedKFold(y, n_folds=n_folds):
        probas = clf.fit(X[train], y[train]).predict_proba(X[test])
        # Compute ROC curve and area the curve
        fpr, tpr, thresholds = metrics.roc_curve(y[test], probas[:, 1])
        mean_tpr += interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0
    mean_tpr /= n_folds
    return [Model.PerformanceStatistics.ROCPoint(
        falsePositiveRate=fpr,
        truePositiveRate=tpr) for (fpr, tpr) in zip(mean_fpr, mean_tpr)]
