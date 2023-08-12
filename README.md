# Image Classification API

This is an image classification API built using FastAPI and TensorFlow/Keras. It allows users to upload images and receive predictions about the contents of the images.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running Locally](#running-locally)
  - [Docker](#docker)
- [API Endpoints](#api-endpoints)
- [Input and Output](#input-and-output)
- [Model](#model)
- [Dependencies](#dependencies)

## Overview

This API provides an interface for image classification using a pre-trained ResNet50 model from TensorFlow/Keras. Users can submit an image URL through an HTTP POST request and receive predictions about the classes present in the image.

## Getting Started

### Installation

1. Clone this repository.
    ```bash
    git clone https://github.com/yourusername/image-classification-api.git
    cd image-classification-api
    ```

2. Create a virtual environment (optional but recommended).
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required packages.
    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

1. Start the FastAPI application.
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```
2. Access the API at `http://localhost:8000`.


### Docker

1. Build the Docker image.
    ```bash
    docker build -t image-classification-api .
    ```
2. Run the Docker container.
    ```bash
    docker run -d -p 8000:80 image-classification-api
    ```
3. Access the API at `http://localhost:8000`.

## API Endpoints

- **POST /classify_image/**
  - Request Body: Specify the user's ID and the image URL.
    ```bash
    {
      "user_id": "123",
      "image_url": "https://example.com/image.jpg"
    }
    ```
  - Response Body: Get a list of predicted classes and their probabilities.
    ```bash
    {
      "user_id": "123",
      "prediction": [
        {
          "className": "dog",
          "probability": 0.92
        },
        {
          "className": "cat",
          "probability": 0.07
        },
        ...
      ]
    }
    ```

## Input and Output

- **Input**: The API accepts a JSON payload containing the user's ID and the URL of the image to classify.
- **Output**: The API responds with a JSON object containing the user's ID and a list of predicted classes along with their probabilities.

## Model

The API uses a pre-trained ResNet50 model from TensorFlow/Keras for image classification. The model has been fine-tuned on the ImageNet dataset.

## Dependencies

The application's dependencies are listed in the `requirements.txt` file. They include FastAPI, TensorFlow/Keras, requests, Pillow, numpy, validators, and base64. You can install them using the command.
    
  ```bash
  pip install -r requirements.txt
  ```