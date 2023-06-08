import numpy as np
from flask import Flask, request, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("DS_Project.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    dependents = int(request.form["box1"])
    education = request.form["box2"]
    self_employed = request.form["box3"]
    applicant_income = float(request.form["box4"])
    coapplicant_income = float(request.form["box5"])
    loan_amount = float(request.form["box6"])
    loan_amount_term = float(request.form["box7"])
    credit_history = float(request.form["box8"])
    property_area = request.form["box9"]
    
    features = np.array([[dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount,
                          loan_amount_term, credit_history, property_area]])
    
    prediction = model.predict(features)
    loan_status = "Approved" if prediction == 1 else "Not Approved"
    
    return render_template("index.html", loan_status=loan_status)

if __name__ == "__main__":
    app.run(debug=True)
