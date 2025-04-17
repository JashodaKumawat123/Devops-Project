#!/bin/bash

# Set version here manually
MODEL_VERSION="v1.0"
MODEL_FILE="model_${MODEL_VERSION}.pkl"

echo "📌 Training model..."
python train_model.py

echo "🐳 Building Docker image..."
docker build -t ml-api:$MODEL_VERSION .

echo "🛑 Stopping old container..."
docker stop ml-api-container || true
docker rm ml-api-container || true

echo "🚀 Running new container..."
docker run -d -p 5000:5000 --name ml-api-container ml-api:$MODEL_VERSION

echo "✅ Deployed model version $MODEL_VERSION!"
