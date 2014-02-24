import unittest
import report
import cPickle
from sklearn import linear_model
import util.random_data as random_data


class TestReport(unittest.TestCase):
    def setUp(self):
        self.X, self.Y = zip([random_data.label_feature_pair() for _ in range(100)])

    def test_serialized(self):
        clf = linear_model.LogisticRegression()
        ser = report.serialized(clf)
        cPickle.loads(ser)
        clf == ser
