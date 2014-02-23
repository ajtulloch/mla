import gen.protobufs.ml_pb2 as ml_pb2
import numpy as np


def random_online_request(num_features):
        return ml_pb2.OnlineTrainRequest(
            features=list(np.random.random(num_features)),
            label=bool(np.random.choice([True, False])))


def random_batch_training_request(num_features, num_examples):
    return ml_pb2.BatchTrainRequest(
        trainingData=ml_pb2.TrainingData(
            source=ml_pb2.INLINE,
            inlineData=[random_online_request(num_features)
                        for _ in range(num_examples)]))
