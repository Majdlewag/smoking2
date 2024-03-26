from fastapi import FastAPI
import pickle
from package_folder.utils import floatingg
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import OneHotEncoder


#path1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models","label_pre.pkl")
#print(path1)

app = FastAPI()

@app.get("/")
def root():
    return {'greeting':"hello"}

@app.get("/predictMult")
def predict(a,b):

    return float(a)*float(b)


@app.get("/predict")
def predict(F1,F2h,F3,F4,F5,F6,F7,F8,F9,F10,
            F11,F12,F13,F14,F15,F16,F17,F18,
            F19,F20,F21,F22,F23,F24h,F25,F26h):

    new_data = floatingg([F1,F3,F4,F5,F6,F7,F8,F9,F10,
                F11,F12,F13,F14,F15,F16,F17,F18,
                F19,F20,F21,F22,F23,F25])# make a TUPLE!!!!!!!!!! faster lighter
    new_data2 = [F2h,F24h,F26h]

    new_data.insert(1,new_data2[0])
    new_data.insert(23,new_data2[1])
    new_data.insert(25,new_data2[2])

    new_data = pd.DataFrame([new_data],columns=['ID', 'gender', 'age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'eyesight(left)', 'eyesight(right)', 'hearing(left)', 'hearing(right)', 'systolic', 'relaxation', 'fasting blood sugar', 'Cholesterol', 'triglyceride', 'HDL', 'LDL', 'hemoglobin', 'Urine protein', 'serum creatinine', 'AST', 'ALT', 'Gtp', 'oral', 'dental caries', 'tartar'])


    #new_data_resized = new_data.T
    #print(new_data.shape)




    #Step1
    #path1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models","label_pre.pkl")
    #labeler = pickle.load(path1)

    #with open('../models/label_pre.pkl', 'rb') as file:
    #    labeler = pickle.load(file)

    #labeler.transform(new_data[['gender']]) # needs re-defining? ,'oral', 'tartar'4
    #labeler.transform(new_data[['oral']])
    #labeler.transform(new_data[['tartar']])
    #print(new_data.head())

    ohe = OneHotEncoder(drop='if_binary',sparse=False, handle_unknown='ignore')
    new_data[["gender","oral","tartar"]] = ohe.fit_transform(new_data[["gender","oral","tartar"]])


    #Step2

    with open('m_work/models/scale_pre.pkl', 'rb') as file:
        scaler = pickle.load(file)
    #path2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models","scale_pre.pkl")
    #scaler = pickle.load(path2)

    scaler.transform(new_data)

    #Step3 predict
    with open('m_work/models/model_pre.pkl', 'rb') as file:
        model = pickle.load(file)
    #path3 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models","model_pre.pkl")
    #model = pickle.load(path3)

    prediction = model.predict(new_data)

    return {"prediction": float(prediction[0])}

    '''
    #pretty_prediction = from_number_to_flower(float(prediction[0]))

    #sample datapoint feed processed already
    samp = pd.read_csv('sample_datapoint.csv')
    samp_resh = np.reshape(samp.iloc[1,:],(1,26))
    samp_pred = model.predict(samp_resh)[0]
    '''
