# prettyplotlib imports
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpltools import style
style.use('ggplot')

from sklearn import linear_model
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer
from sklearn import svm, cross_validation

import numpy as np
import logging

log = logging.getLogger(__name__)

METRICS = ['accuracy', 'average_precision', 'f1',
           'log_loss', 'precision', 'recall', 'roc_auc']


class Reporter(object):
    @staticmethod
    def report(train_requests):
        results = {}
        X = np.array([list(r.features) for r in train_requests])
        y = np.array([r.label for r in train_requests])
        log.info("X: %s, y: %s", X, y)
        for metric in METRICS:
            log.info("Computing metric: %s", metric)
            scores = cross_validation.cross_val_score(
                linear_model.LogisticRegression(), X, y, scoring=metric)
            results[metric] = np.mean(scores)
            log.info("Metric: %s", scores)
        return results
