from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")

def root():
    return {'Greeting ':"Hello"}


@app.get("/predict")

def predict(x1,
            x2,
            x3,
            x4):
    # remember to put models directory in root directly!!!
    with open('models/best_model.pkl','rb') as file:
        model = pickle.load(file)

    prediction = model.predict([[1,2,3,4]])
    return {"prediction": float(prediction[0])}
