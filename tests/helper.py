from src.utils.test_images import image_links
import json
from src.schemas.image_schema import Img


def predict_test(client, api_url, num_image):

    sample = Img(url_image=image_links[num_image]['url'])
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    res = client.post(api_url,
                      data=json.dumps(sample.dict()),
                      headers=headers)

    return res.json()