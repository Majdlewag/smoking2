from fastapi import FastAPI, File, UploadFile
import pickle
from package_folder.utils import floatingg
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import OneHotEncoder

from tensorflow.keras.models import load_model
#from keras.preprocessing.image import load_img
#from keras.preprocessing.image import img_to_array
# instead of
from tensorflow.keras.utils import load_img
#from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.utils import img_to_array

from PIL import Image ################ ooooooooooooooooooooooo

#import requests
#import time
#import io
#import shutil




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
    #new_data = pd.to_numeric(new_data)
    new_data2 = [F2h,F24h,F26h]

    new_data.insert(1,new_data2[0])
    new_data.insert(23,new_data2[1])
    new_data.insert(25,new_data2[2])

    new_data = pd.DataFrame([new_data],columns=['ID', 'gender', 'age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'eyesight(left)', 'eyesight(right)', 'hearing(left)', 'hearing(right)', 'systolic', 'relaxation', 'fasting blood sugar', 'Cholesterol', 'triglyceride', 'HDL', 'LDL', 'hemoglobin', 'Urine protein', 'serum creatinine', 'AST', 'ALT', 'Gtp', 'oral', 'dental caries', 'tartar'])


    #Step1
    #path1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models","label_pre.pkl")
    #labeler = pickle.load(path1)

    #with open('models/label_pre.pkl', 'rb') as file:
    #    labeler = pickle.load(file)

    #labeler.transform(new_data[['gender']]) # needs re-defining? ,'oral', 'tartar'4
    #labeler.transform(new_data[['oral']])
    #labeler.transform(new_data[['tartar']])
    #print(new_data.head())


    with open("models/ohe_pre.pkl", 'rb') as file:
        oher = pickle.load(file)
    #ohe = OneHotEncoder(drop='if_binary',sparse=False, handle_unknown='ignore')
    #new_data[["gender","oral","tartar"]] = ohe.fit_transform(new_data[["gender","oral","tartar"]])
    new_data[["gender","oral","tartar"]] = oher.transform(new_data[["gender","oral","tartar"]])
    #new_data[["gender","oral","tartar"]] =


    #Step2
    #print("YEEEEEEEEEEEEEEESSSSSSSSSSSSSSSSSSSSSSSSSSSS???????????????????")
    with open("models/scale_pre.pkl", 'rb') as file:
        scaler = pickle.load(file)
    #path2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models","scale_pre.pkl")
    #print(path2)
    #scaler = pickle.load(path2)
    #print("abcdjknvsknfskbnfs!!!!!!!!!!!!???????????????????")
    scaler.transform(new_data)

    #Step3 predict
    with open('models/model_pre.pkl', 'rb') as file:
        model = pickle.load(file)
    #path3 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models","model_pre.pkl")
    #model = pickle.load(path3)
    print("aaaaaaaaaaaaaaaaaaaaaabbbsdkjvdfnvdfvdkjnvdfkjnfdjaaaaaaaaaaaaaaaaaaaaa")
    prediction = model.predict(new_data)
    print(prediction)
    return {"prediction": float(prediction[0])}



@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    #image_path = "package_folder/Malignant case (570).jpg"
    #image_path = "package_folder/Normal case (420).jpg"

    #file_path = os.path.abspath(immmage)
    # Load the image and resize it to the desired size
    with open('temp_image.jpg', 'wb') as f:
        f.write(file.file.read())
    image = Image.open('temp_image.jpg')
    img = load_img('temp_image.jpg', target_size=(224, 224, 3),)#target_size
    #image = image.resize((224,224))
    #img = load_img(("package_folder/" + file.filename), target_size=(224, 224, 3),)#target_size
    #img = image_dataset_from_directory(("package_folder/" + file.filename), labels=None,color_mode="rgb",batch_size=1,image_size=(224, 224),)

    #img = image_dataset_from_directory(("package_folder/" + file.filename), labels=None,color_mode="rgb",batch_size=1,image_size=(224, 224),)#target_size

    # Convert the image to a numpy array
    img_array = img_to_array(img)
    img_array = img_array/255

    # If your model expects a batch, you need to add an extra dimension
    # This changes the shape from (150, 150, 3) to (1, 150, 150, 3)
    img_array = np.expand_dims(img_array, axis=0)

    #load model
    modelll = load_model("package_folder/CNN(Custom).keras")#adjust pathhhhhhhh?????
    #modelll2 = load_model("package_folder/CNN(Custom5).keras")


    # Now you can pass an image to the predict method
    predictions = modelll.predict(img_array)
    #predictions2 = modelll2.predict(img_array)

    #print(predictions)
    #print(type(predictions))
    #print(predictions2)##############################################
    #####################################################comment out

    if predictions[0].argmax() == 0:
        answer = "0, Benign- Phew!"
    elif predictions[0].argmax() == 1:
        answer = "1, Malignant!"
    else:
        answer = "2, Normal- Nothing Here"
    return {"prediction": str(answer)}

    #return {"prediction": float(answer)}
    #return {"filename": file.filename}
    #['Bengin cases', 'Malignant cases', 'Normal cases']
