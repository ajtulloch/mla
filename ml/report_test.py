import unittest
import report
import cPickle
from sklearn import linear_model
import util.random_data as random_data
import numpy as np

NUM_FEATURES = 10
NUM_EXAMPLES = 100


class TestReport(unittest.TestCase):
    def setUp(self):
        online_train_requests = [random_data.online_request(NUM_FEATURES)
                                 for _ in range(NUM_EXAMPLES)]
        self.X = np.array([list(r.features) for r in online_train_requests])
        self.y = np.array([r.label for r in online_train_requests])

    def test_serialized(self):
        clf = linear_model.LogisticRegression()
        clf.fit(self.X, self.y)
        ser = report.serialized(clf)
        clfDeserialized = cPickle.loads(ser.pickledString)
        self.assertTrue(
            np.array_equal(clf.predict(self.X), clfDeserialized.predict(self.X)))

if __name__ == '__main__':
    unittest.main()
