# backend/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import tensorflow as tf
import numpy as np
from io import BytesIO

from transformers import ViTForImageClassification, ViTImageProcessor
from timm import create_model

import torch
import torch.nn.functional as F
import torchvision
import torchvision.transforms as T

from huggingface_hub import hf_hub_download

app = FastAPI()

# CORS for frontend access
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # or restrict to your domain
  allow_methods=["*"],
  allow_headers=["*"],
)

class_names = ['cordana', 'healthy', 'pestalotiopsis', 'sigatoka'] 

current_model_type = None
vit_model = None
cnn_model = None

def unload_cnn():
  global cnn_model
  if cnn_model is not None:
    tf.keras.backend.clear_session()
    cnn_model = None
    print("CNN model unloaded")

def unload_vit():
  global vit_model
  if vit_model is not None:
    vit_model = None
    torch.cuda.empty_cache()
    print("ViT model unloaded")

@app.post("/set-model")
async def set_model(model_name: str):
  global current_model_type, cnn_model, vit_model

  if model_name.lower() not in ["cnn", "vit"]:
    return {"error": "Invalid model name. Use 'cnn' or 'vit'."}

  # Unload existing model if different
  if current_model_type == "cnn" and model_name != "cnn":
    unload_cnn()
  elif current_model_type == "vit" and model_name != "vit":
    unload_vit()

  # Load new model
  if model_name.lower() == "cnn" and cnn_model is None:
    print("Loading CNN model...")
    cnn_model = tf.keras.models.load_model("models/cnn_banana_leaf_disease_classifier.keras")
    cnn_model.make_predict_function()
    print("CNN model loaded.")
  elif model_name.lower() == "vit" and vit_model is None:
    print("Loading ViT model...")
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print("Using device:", device)
    vit_model = create_model("vit_tiny_patch16_224", pretrained=False, num_classes=4).to(device)
    vit_model.load_state_dict(torch.load("models/vit_base_0.01.pth", map_location=device))
    vit_model.eval()
    print("ViT model loaded.")

  current_model_type = model_name.lower()
  return {"message": f"{model_name} model is now active."}

IMG_SIZE = (224, 224)
NORMALIZE_MEAN = (0.5, 0.5, 0.5)
NORMALIZE_STD = (0.5, 0.5, 0.5)
transforms = [
  T.Resize(IMG_SIZE),
  T.ToTensor(),
  T.Normalize(NORMALIZE_MEAN, NORMALIZE_STD),
]

transforms = T.Compose(transforms)

def preprocess_image(image: Image.Image) -> np.ndarray:
  image = image.resize((224, 224))  
  image = np.array(image) / 255.0 
  image = np.expand_dims(image, axis=0)
  return image

@app.post("/cnn-classify")
async def cnn_classify(file: UploadFile = File(...)):
  try:
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    preprocessed = preprocess_image(image)

    predictions = cnn_model.predict(preprocessed)
    predicted_index = np.argmax(predictions)
    label = class_names[predicted_index]
    confidence = float(np.max(predictions))

    return {
      "class": label,
      "confidence": confidence
    }

  except Exception as e:
    return {"error": str(e)}
  
@app.post("/vit-classify")
async def vit_classify(file: UploadFile = File(...)):
  try:
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    input_tensor = transforms(image).unsqueeze(0).to(device)

    with torch.no_grad():
      outputs = vit_model(input_tensor)
      probabilities = torch.nn.functional.softmax(outputs, dim=1)
      predicted_index = torch.argmax(probabilities, dim=1).item()
      label = class_names[predicted_index]
      confidence = probabilities[0][predicted_index].item()

    return {"class": label, "confidence": confidence}

  except Exception as e:
      return {"error": str(e)}

@app.get("/")
def root():
  return {"message": "API is running"}