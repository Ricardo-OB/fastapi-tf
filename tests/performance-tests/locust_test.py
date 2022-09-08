from locust import HttpUser, task, between
from src.schemas.image_schema import Img
import json
from tests.helper import predict_test

class PerformanceTests(HttpUser):
    wait_time = between(1,3)

    @task(1)
    def test_tf_predict1(self):
        res = predict_test(self.client, api_url='/predict/tf/', num_image=0)
        print('res', res)

    @task(2)
    def test_tf_predict2(self):
        res = predict_test(self.client, api_url='/predict/tf/', num_image=1)
        print('res', res)