from crypt import methods
import pickle
from types import MethodType
from flask import Flask ,request,render_template,jsonify,url_for
import numpy as np
import pandas as pd  
app = Flask(__name__)
# Load the model
regmodel = pickle.load(open('regmodel.pkl','wb'))
scaler = pickle.load(open('regmodel.pkl','wb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict_api',methods = ['post'])
def predict_api():
    
