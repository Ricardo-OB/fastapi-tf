from fastapi import FastAPI, HTTPException
from schemas.image_schema import Img
from preds.image_classifier import tf_run_classifier

app = FastAPI(title='Image Classifier API')

@app.post('/predict/tf', status_code=200)
async def predict(request: Img):
    prediction = tf_run_classifier(request.url_image)

    if not prediction:
        raise HTTPException(
            status_code=404,
            detail="Image couldnt be downloaded"
        )

    return prediction