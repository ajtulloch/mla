import requests
import random
import gen.protobufs.ml_pb2 as pb
from protobuf_to_dict import protobuf_to_dict
import json

def fake_data(name, num_examples, num_features):
    def fake_example():
        return protobuf_to_dict(pb.TrainRequest(
            label=bool(random.getrandbits(1)),
            features=[random.random() for _ in range(num_features)]
        ))

    return {
        'name': name,
        'examples': [fake_example() for _ in range(num_examples)]
    }

    
    
requests.post(
    "http://localhost:5000/mlserver/datasets",
    data=json.dumps(fake_data(name='apples', num_examples=50, num_features=2)),
    headers={'content-type': 'application/json'}
)
