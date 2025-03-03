from app import model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict/")
def predict_iris(data: IrisRequest):
    features = [data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]
    prediction = model.predict(features)
    return {"prediction": prediction}
