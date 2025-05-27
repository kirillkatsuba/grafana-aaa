from fastapi import FastAPI, Query
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import random
import time

app = FastAPI()

REQUEST_COUNT = Counter("request_count", "Total requests", ["model_type", "gender", "status"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency", ["model_type", "gender"])

@app.get("/predict")
def predict(model_type: str = Query("e5"), gender: str = Query("male")):
    start_time = time.time()
    # Имитация работы модели и инференса
    time.sleep(random.uniform(0.05, 0.2))
    latency = time.time() - start_time

    REQUEST_LATENCY.labels(model_type=model_type, gender=gender).observe(latency)

    # Случайная ошибка 5%
    if random.random() < 0.05:
        REQUEST_COUNT.labels(model_type=model_type, gender=gender, status="error").inc()
        return {"error": "something went wrong"}
    else:
        REQUEST_COUNT.labels(model_type=model_type, gender=gender, status="success").inc()
        prob = random.uniform(0, 1)
        return {"probability": prob, "model_type": model_type, "gender": gender}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

