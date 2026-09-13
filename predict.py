import joblib
import numpy as np

# ============================================================
# TẢI MÔ HÌNH ĐÃ TRAIN
# ============================================================

model = joblib.load("attrition_model.pkl")

# ============================================================
# NHÂN VIÊN MỚI CẦN DỰ ĐOÁN
# ============================================================
# Nhân viên:
# Tuổi: 28
# Thu nhập hàng tháng: 3500
# Hài lòng công việc: 2/4
# Làm thêm giờ: Có
# Số năm tại công ty: 2
# Khoảng cách từ nhà: 20 km
# Work-life balance: 2/4
# Hài lòng môi trường: 2/4
# Số công ty từng làm: 4
# ============================================================

nhan_vien_moi = np.array([
    [28, 3500, 2, 1, 2, 20, 2, 2, 4]
])

# ============================================================
# DỰ ĐOÁN
# ============================================================

prediction = model.predict(nhan_vien_moi)

# ============================================================
# HIỂN THỊ KẾT QUẢ
# ============================================================

if prediction[0] == 1:
    ket_qua = "Yes"
    thong_bao = "Nhân viên có khả năng nghỉ việc"
else:
    ket_qua = "No"
    thong_bao = "Nhân viên có khả năng tiếp tục làm việc"

print("======================================")
print("   DỰ ĐOÁN NHÂN VIÊN NGHỈ VIỆC")
print("======================================")

print("Tuổi:", nhan_vien_moi[0][0])
print("Thu nhập hàng tháng:", nhan_vien_moi[0][1])
print("Mức độ hài lòng công việc:", nhan_vien_moi[0][2])
print("Làm thêm giờ:", "Có" if nhan_vien_moi[0][3] == 1 else "Không")
print("Số năm tại công ty:", nhan_vien_moi[0][4])
print("Khoảng cách từ nhà:", nhan_vien_moi[0][5], "km")
print("Cân bằng công việc/cuộc sống:", nhan_vien_moi[0][6])
print("Hài lòng môi trường:", nhan_vien_moi[0][7])
print("Số công ty từng làm:", nhan_vien_moi[0][8])

print("--------------------------------------")
print("Kết quả dự đoán:", ket_qua)
print("Thông báo:", thong_bao)
print("======================================")