# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Bước 1: Load và chuẩn bị dữ liệu
# Load dữ liệu từ file CSV
file_path = 'C:/Users/ADMIN/PycharmProjects/demo/sales_data (1).csv'
sales_data = pd.read_csv(file_path)


sales_data = sales_data.head(200)

# Kiểm tra cấu trúc dữ liệu
print(sales_data.info())

# Bước 2: Trực quan hóa dữ liệu
# Tạo biểu đồ phân tán giữa số lượng bán và tổng giá trị đơn hàng
plt.figure(figsize=(8, 4))
plt.scatter(sales_data['Quantity'], sales_data['TotalPrice'], color='orange', label='Data Points')
plt.title('Scatter Plot: Quantity vs TotalPrice')
plt.xlabel('Quantity Sold')
plt.ylabel('Total Price')
plt.grid(True)
plt.show()

# Bước 3: Tạo mô hình hồi quy tuyến tính
# Chọn biến độc lập (Quantity) và biến phụ thuộc (TotalPrice)
X = sales_data[['Quantity']]
y = sales_data['TotalPrice']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Khởi tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán giá trị trên tập kiểm tra
y_pred = model.predict(X_test)

# Bước 4: Vẽ biểu đồ hồi quy tuyến tính
# Vẽ các điểm dữ liệu và đường hồi quy trên cùng một biểu đồ
plt.figure(figsize=(8, 4))
plt.scatter(X_test, y_test, color='orange', label='Data Points')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.title('Linear Regression')
plt.xlabel('Quantity')
plt.ylabel('Total Price')
plt.legend()
plt.grid(True)
plt.show()


# Bước 5: Đánh giá mô hình
# Hiển thị kết quả mô hình
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')
print(f'R-squared: {r2_score(y_test, y_pred)}')
print(f'Coefficient: {model.coef_[0]}')
print(f'Intercept: {model.intercept_}')
