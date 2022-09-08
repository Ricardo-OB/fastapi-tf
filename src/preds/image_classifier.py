from src.preds.models.tf_pred import tf_predict
from typing import Any
from src.utils.utilities import load_image

def tf_run_classifier(image: str) -> Any:
    img = load_image(image)
    if img is None:
        return None
    pred_results = tf_predict(img)
    return pred_results