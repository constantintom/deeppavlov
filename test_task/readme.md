docker exec -it dp_docker_flask_flask_1 bash
docker exec -it dp_docker_flask_flask_1 python train_model.py
curl --header "Content-Type: application/json" --request POST --data '{"method": "upper", "text": "sTrInG"}' http://0.0.0.0:5000/model
curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "upper", "text": "sTrInG"}'
curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "upper", "text": "sTrInG"}'
curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "lower", "text": "sTrInG"}' 
curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "swapcase", "text": "sTrInG"}'