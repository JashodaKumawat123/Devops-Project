# # train_model.py
# import joblib
# import os
# from sklearn.datasets import load_iris
# from sklearn.ensemble import RandomForestClassifier

# # Set the version manually
# model_version = "v5.0"
# model_filename = f"model_{model_version}.pkl"

# # Train the model
# iris = load_iris()
# X, y = iris.data, iris.target

# model = RandomForestClassifier()
# model.fit(X, y)

# # Save the model with version
# joblib.dump(model, model_filename)

# # Save version to a text file
# with open("version.txt", "w") as f:
#     f.write(model_version)

# print(f"Model saved as {model_filename} with version {model_version}")
# train_model.py
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import os

# Set the version manually
model_version = "v5.0"

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X, y)
rf_filename = f"model_rf_{model_version}.pkl"
joblib.dump(rf_model, rf_filename)

# Train Support Vector Machine
svm_model = SVC(probability=True)  # probability=True if you plan to use predict_proba
svm_model.fit(X, y)
svm_filename = f"model_svm_{model_version}.pkl"
joblib.dump(svm_model, svm_filename)

# Save version to a text file
with open("version.txt", "w") as f:
    f.write(model_version)

print(f"Random Forest model saved as {rf_filename}")
print(f"SVM model saved as {svm_filename}")
print(f"Model version saved as {model_version}")

