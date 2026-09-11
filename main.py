from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="House Price Prediction API")

# Load mô hình Bagging đã tạo
model = joblib.load("bagging_model.pkl")

class HouseRequest(BaseModel):
    dientich: float
    so_phong_ngu: int

@app.get("/")
def home():
    return {"message": "API Dự đoán giá nhà đang hoạt động!"}

@app.post("/predict")
def predict(data: HouseRequest):
    input_data = np.array([[data.dientich, data.so_phong_ngu]])
    prediction = model.predict(input_data)
    return {
        "dientich": data.dientich,
        "so_phong_ngu": data.so_phong_ngu,
        "gia_du_doan_ty": round(float(prediction[0]), 2)
    }