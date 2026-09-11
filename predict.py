import joblib
import numpy as np

# Tải mô hình Bagging đã lưu
model = joblib.load("bagging_model.pkl")

# Căn nhà mới cần định giá: Diện tích 70m2, 3 phòng ngủ
nha_moi = np.array([[70, 3]])

# Dự đoán (Mô hình sẽ tính trung bình kết quả của 100 cây con)
gia_du_doan = model.predict(nha_moi)

print(f"Dự đoán giá nhà (70m2, 3 phòng ngủ): {gia_du_doan[0]:.2f} tỷ VNĐ")