import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Dữ liệu huấn luyện: [Diện tích (m2), Số phòng ngủ]
X = np.array([
    [30, 1],
    [45, 2],
    [60, 2],
    [80, 3],
    [100, 4]
])

# Giá nhà tương ứng (tỷ VNĐ)
y = np.array([1.5, 2.3, 3.1, 4.0, 5.2])

# Khởi tạo Bagging với 100 cây quyết định con
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Huấn luyện mô hình
model.fit(X, y)

# Lưu mô hình đã train ra file .pkl
joblib.dump(model, "bagging_model.pkl")
print("Đã huấn luyện xong mô hình Bagging và lưu thành file 'bagging_model.pkl'!")