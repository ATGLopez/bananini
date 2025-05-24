# backend/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import tensorflow as tf
import numpy as np
from io import BytesIO

app = FastAPI()
BASE_URL = "https://bananini.onrender.com"

# CORS for frontend access
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # or restrict to your domain
  allow_methods=["*"],
  allow_headers=["*"],
)

print('\nLoading classifiers...\n')

# Load model and feature extractor
model = tf.keras.models.load_model("cnn_banana_leaf_disease_classifier.keras")

if model:
  print('\nClassifiers loaded successfully.\n')
  
model.make_predict_function() 

# Define the label mapping (must match training order!)
class_names = ['cordana', 'healthy', 'pestalotiopsis', 'sigatoka']  # Adjust if needed

# Image preprocessing function
def preprocess_image(image: Image.Image) -> np.ndarray:
    image = image.resize((224, 224))  # or (img_size, img_size) used in training
    image = np.array(image) / 255.0   # normalize to [0, 1]
    image = np.expand_dims(image, axis=0)  # batch dimension
    return image

# POST endpoint to classify uploaded image
@app.post("{BASE_URL}/cnn-classify")
async def cnn_classify(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(BytesIO(contents)).convert("RGB")
        preprocessed = preprocess_image(image)

        predictions = model.predict(preprocessed)
        predicted_index = np.argmax(predictions)
        label = class_names[predicted_index]
        confidence = float(np.max(predictions))

        return {
            "class": label,
            "confidence": confidence
        }

    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def root():
  return {"message": "API is running"}