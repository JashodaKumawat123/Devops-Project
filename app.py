



from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the /version route to check model version
@app.route('/version', methods=['GET'])
def version():
    return jsonify({"version": "v4.0"})

# Define the /predict route to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Your prediction logic here
    return jsonify({"prediction": "result"})

# Default route for root (optional)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the ML API!"

if __name__ == '__main__':
    # Make sure to run the app on 0.0.0.0 (accessible externally)
    app.run(host='0.0.0.0', port=5000)
