import unittest
from report import ProtobufReporter, serialized
import cPickle
from sklearn import linear_model
import util.random_data as random_data
import numpy as np

NUM_FEATURES = 10
NUM_EXAMPLES = 50


class TestReport(unittest.TestCase):
    def setUp(self):
        online_train_requests = [random_data.online_request(NUM_FEATURES)
                                 for _ in range(NUM_EXAMPLES)]
        self.online_train_requests = online_train_requests
        self.X = np.array([list(r.features) for r in online_train_requests])
        self.y = np.array([r.label for r in online_train_requests])

    def test_serialized(self):
        clf = linear_model.LogisticRegression()
        clf.fit(self.X, self.y)
        ser = serialized(clf)
        clfDeserialized = cPickle.loads(ser.pickledString)
        self.assertTrue(
            np.array_equal(clf.predict(self.X),
                           clfDeserialized.predict(self.X)))

    def test_construction(self):
        report = ProtobufReporter().build(self.online_train_requests)
        self.assertEquals(report.summaryStatistics.numExamples,
                          len(self.online_train_requests))
        self.assertEquals(report.summaryStatistics.numPositives,
                          sum(1 for el in self.y if el))

if __name__ == '__main__':
    unittest.main()
