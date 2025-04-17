# Use slim Python image
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all code
COPY . .

# Run the app
CMD ["python", "app.py"]
