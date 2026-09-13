from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# ============================================================
# KHỞI TẠO FASTAPI
# ============================================================

app = FastAPI(
    title="Employee Attrition Prediction API",
    description="API dự đoán khả năng nhân viên nghỉ việc bằng Random Forest",
    version="1.0.0"
)

# ============================================================
# LOAD MÔ HÌNH
# ============================================================

model = joblib.load("attrition_model.pkl")


# ============================================================
# ĐỊNH NGHĨA DỮ LIỆU ĐẦU VÀO
# ============================================================

class EmployeeRequest(BaseModel):

    age: int

    monthly_income: float

    job_satisfaction: int

    overtime: int

    years_at_company: int

    distance_from_home: float

    work_life_balance: int

    environment_satisfaction: int

    num_companies_worked: int


# ============================================================
# TRANG CHỦ
# ============================================================

@app.get("/")
def home():

    return {
        "message": "API Dự đoán nhân viên nghỉ việc đang hoạt động!"
    }


# ============================================================
# API DỰ ĐOÁN
# ============================================================

@app.post("/predict")
def predict(data: EmployeeRequest):

    # --------------------------------------------------------
    # Chuyển dữ liệu đầu vào thành mảng NumPy
    # --------------------------------------------------------

    input_data = np.array([
        [
            data.age,
            data.monthly_income,
            data.job_satisfaction,
            data.overtime,
            data.years_at_company,
            data.distance_from_home,
            data.work_life_balance,
            data.environment_satisfaction,
            data.num_companies_worked
        ]
    ])

    # --------------------------------------------------------
    # Dự đoán
    # --------------------------------------------------------

    prediction = model.predict(input_data)

    # --------------------------------------------------------
    # Lấy xác suất dự đoán
    # --------------------------------------------------------

    probability = model.predict_proba(input_data)

    probability_no = probability[0][0]
    probability_yes = probability[0][1]

    # --------------------------------------------------------
    # Chuyển kết quả thành Yes / No
    # --------------------------------------------------------

    if prediction[0] == 1:

        attrition = "Yes"

        message = "Nhân viên có khả năng nghỉ việc"

    else:

        attrition = "No"

        message = "Nhân viên có khả năng tiếp tục làm việc"

    # --------------------------------------------------------
    # Trả về kết quả
    # --------------------------------------------------------

    return {

        "age": data.age,

        "monthly_income": data.monthly_income,

        "job_satisfaction": data.job_satisfaction,

        "overtime": data.overtime,

        "years_at_company": data.years_at_company,

        "distance_from_home": data.distance_from_home,

        "work_life_balance": data.work_life_balance,

        "environment_satisfaction": data.environment_satisfaction,

        "num_companies_worked": data.num_companies_worked,

        "attrition_prediction": attrition,

        "probability_no": round(float(probability_no), 4),

        "probability_yes": round(float(probability_yes), 4),

        "message": message
    }