import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app=Flask(__name__)

model= pickle.load(open("DS_Project.pkl","rb"))

@app.route("/")
def Home():
    return render_template("")