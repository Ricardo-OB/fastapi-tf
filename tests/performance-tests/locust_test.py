from locust import HttpUser, task, between
from src.schemas.image_schema import Img
import json

class PerformanceTests(HttpUser):
    wait_time = between(1,3)

    @task(1)
    def test_tf_predict(self):
        sample = Img(url_image='https://raw.githubusercontent.com/pytorch/hub/master/images/dog.jpg')
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
        res = self.client.post("/predict/tf/",
                               data=json.dumps(sample.dict()),
                               headers=headers)
        print("res", res.json())