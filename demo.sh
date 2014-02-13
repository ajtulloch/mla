curl -X POST -H "Content-Type: application/json" -d '{"features":[1,2,3], "label":true}' http://localhost:5000/train
curl -X POST -H "Content-Type: application/json" -d '{"features":[1,2,3]}' http://localhost:5000/predict

