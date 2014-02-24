import gen.protobufs.ml_pb2 as ml_pb2
import numpy as np


def label_feature_pair(num_features):
    features = list(np.random.random(num_features))
    label = bool(np.random.choice([True, False]))
    return (label, features)


def online_request(num_features):
    (label, features) = label_feature_pair(num_features)
    return ml_pb2.OnlineTrainRequest(features=features, label=label)


def batch_training_request(num_features, num_examples):
    return ml_pb2.BatchTrainRequest(
        trainingData=ml_pb2.TrainingData(
            source=ml_pb2.INLINE,
            inlineData=[online_request(num_features)
                        for _ in range(num_examples)]))
