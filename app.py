from flask import Flask, render_template

# Initialize the Flask Application
app = Flask(__name__)

# --- Route 1: The Home Page ---
# This is what the user sees when they open the website.
@app.route('/')
def home():
    # For now, we return a simple HTML string. Later, this will be a real HTML file.
    return """
    <div style="text-align: center; padding-top: 50px; font-family: sans-serif;">
        <h1>Integrated Diabetes Detection System</h1>
        <p>System Status: <strong>Online</strong></p>
        <hr>
        <h3>Available Modules:</h3>
        <p>1. Clinical Prediction (SVC Model) - <em>Ready</em></p>
        <p>2. Retinal Scan Analysis (CNN-SVC Hybrid) - <em>Ready</em></p>
    </div>
    """

# --- Route 2: API for Clinical Data (Pipeline 1) ---
# This listens for data from the "Clinical Form"
@app.route('/predict_clinical', methods=['POST'])
def predict_clinical():
    return "API Endpoint: Clinical Data received. SVC Model is loading..."

# --- Route 3: API for Image Data (Pipeline 2) ---
# This listens for file uploads for the "Image Pipeline"
@app.route('/predict_image', methods=['POST'])
def predict_image():
    return "API Endpoint: Image received. CNN-SVC Hybrid Model is loading..."

# Run the Server
if __name__ == "__main__":
    app.run(debug=True)