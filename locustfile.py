from locust import HttpUser, task, between
import random

class MLUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict(self):
        model_type = random.choice(["e5", "labse"])
        gender = random.choice(["male", "female"])
        self.client.get(f"/predict?model_type={model_type}&gender={gender}")

