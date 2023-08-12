from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from PIL import Image
import numpy as np
from io import BytesIO
import requests
import validators
import base64

app = FastAPI()

# Load the pre-trained ResNet50 model
model = ResNet50(weights='imagenet')

# Define Request Schema
class RequestSchema(BaseModel):
    user_id: str
    image_url: str  # Allow either an image URL or image content

# Define Prediction Schema
class Prediction(BaseModel):
    className: str
    probability: float

# Define Response Schema
class ResponseSchema(BaseModel):
    user_id: str
    prediction: List[Prediction]

@app.post("/classify_image/", response_model=ResponseSchema)
async def classify_image(data: RequestSchema):
    try:
        user_id = data.user_id
        image_url = data.image_url

        # Download the image if it's a valid URL
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))


        # Preprocess the image
        image = image.resize((224, 224))  # ResNet50 input size
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)

        # Make prediction using the model
        predictions = model.predict(image_array)
        decoded_predictions = decode_predictions(predictions, top=5)[0]

        # Convert predictions to desired format
        prediction_results = []
        for class_id, class_name, probability in decoded_predictions:
            prediction_results.append({"className": class_name, "probability": float(probability)})

        result = {
            "user_id": user_id,
            "prediction": prediction_results
        }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
