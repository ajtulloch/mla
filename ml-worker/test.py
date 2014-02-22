import gen.protobufs.ml_pb2 as ml_pb2
import random
import worker


def random_data():
    return ml_pb2.OnlineTrainRequest(
        features=[random.random() for _ in range(100)],
        label=random.choice([True, False]))


def test():
    req = ml_pb2.BatchTrainRequest(
        trainingData=ml_pb2.TrainingData(
            source=ml_pb2.INLINE,
            inlineData=[random_data() for _ in range(100)]))
    return worker.batch_train(req)
