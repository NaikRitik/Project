# Diabetes Detection System (Team Setup Guide) 🏥

This repository contains the **30% Milestone** code for our final year project. It includes the **Flask Web App Skeleton**, the **Clinical Data Model (SVC)**, and the **Image Preprocessing Pipeline**.

---

## 🚀 How to Run This Project on Your Laptop

Follow these 3 steps to get the project running locally.

### Step 1: Install Required Tools
Open your **VS Code Terminal**
```bash
pip install pandas numpy scikit-learn opencv-python matplotlib flask notebook
```

###Step 2: Run the Web App (Flask)
To start the website skeleton:

In the terminal, run:
python app.py
You will see Running on http://127.0.0.1:5000.

###Step 3: Run the Model Experiments
To see the Machine Learning training and Image processing:
Open the file model_demo.ipynb in VS Code.
Click "Run All" at the top.
This will:
Load diabetes.csv.
Clean the data and train the SVC model (Check accuracy output).
Load sample_eye.jpg and resize it for the CNN (Check image plot).

Project Structure (What is What?)
app.py ⚙️
What it is: The main Website file (Backend).
Function: It starts the server and handles the API routes (/predict_clinical and /predict_image). This is where we will eventually connect our trained models.

model_demo.ipynb 🧪
What it is: The Research Notebook.
Function: Used for training and testing. It proves our SVC model works (Accuracy: ~76%) and that our Image Preprocessing (resizing to 224x224) is correct.

diabetes.csv 📊
What it is: The PIMA Indians Diabetes Dataset.
Function: Used to train the SVC model.

sample_eye.jpg 👁️
What it is: A dummy retinal scan.
Function: Used to test if the Image Preprocessing pipeline is working correctly.

✅ Current Progress (30% Milestone)
We have successfully implemented:
Data Pipeline: Handling missing values (Imputation) and Scaling for clinical data.
Baseline Algorithm: SVC (Linear Kernel) achieving >76% accuracy.
Image Pipeline: Converting raw images to RGB and resizing to 224x224 for MobileNetV2.
Web Skeleton: Flask server is online with basic routing established.

🔜 Next Steps for the Team
[ ] Connect the trained SVC model to the Flask front-end.
[ ] Integrate the pre-trained MobileNetV2 weights.
[ ] Build the HTML/CSS pages for the user interface.

