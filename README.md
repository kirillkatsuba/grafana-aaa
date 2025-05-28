# grafana-aaa

Для запуска необходимо следующее:

```
sudo docker-compose up --build -d
```

Затем можно обратиться к модели

```
curl -X POST "http://localhost:8000/predict_gender"
-H "Content-Type: application/json"
-d '{"name": "Alice", "model_type": "lr"}'
```

По следующим ссылка можно посмотреть на нужный сервер:

 - ML service ```http://localhost:8000 ```
 - Grafana ```http://localhost:3000 ```
 - Prometheus ```http://localhost:9090 ```
 - Locust ```http://localhost:8089 ```
