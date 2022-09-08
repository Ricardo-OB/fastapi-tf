from fastapi import FastAPI, HTTPException
from src.schemas.image_schema import Img
from src.preds.image_classifier import tf_run_classifier

app = FastAPI(title='Image Classifier API')

@app.post('/predict/tf', status_code=200)
async def predict(request: Img):
    prediction = tf_run_classifier(request.img_url)

    if not prediction:
        raise HTTPException(
            status_code=404,
            detail="Image couldnt be downloaded"
        )

    return prediction