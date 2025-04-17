# train_model.py
import joblib
import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Set the version manually
model_version = "v5.0"
model_filename = f"model_{model_version}.pkl"

# Train the model
iris = load_iris()
X, y = iris.data, iris.target

model = RandomForestClassifier()
model.fit(X, y)

# Save the model with version
joblib.dump(model, model_filename)

# Save version to a text file
with open("version.txt", "w") as f:
    f.write(model_version)

print(f"Model saved as {model_filename} with version {model_version}")
