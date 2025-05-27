# Bananini

[`Bananini`](https://bananini.vercel.app) is a web application that allows users to upload a photo of a banana leaf for disease diagnosis. It contains two models trained to classify banana leaves into one of four categories: Cordana, Pestalotiopsis, Sigatoka, and Healthy.

The application frontend was built with Svelte + Tailwind CSS. we set up a FastAPI backend, to accommodate requests for image classification.

## Deep Learning Models

The application contains two different deep learning models for classification:

Convolutional Neural Network (CNN)
- The CNN model uses the MobileNetV2 model, pre-trained using the ImageNet-1K dataset, finetuned using a given banana leaf diseases dataset.

Vision Transformer (ViT)
- The Vit model uses the ---

