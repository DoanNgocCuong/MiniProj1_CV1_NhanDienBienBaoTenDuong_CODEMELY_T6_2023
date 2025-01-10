T6/2023: 

Step 1: Collection 
Bộ dataset tự kiếm: 
1. Kiếm Google - Đoàn Ngọc Cường
2. Cắt từ Youtube - Chu Anh 

1. Lịch sử Build Dataset : 4300 tấm == 450 tấm (google Cường code + Cắt Youtube Đức code) * 9 Transformation Data types Cường Transformation -> gói free cần chia ra 3 loại tạo xong gom lại - export YOLOV8 năm đó)
---

Step 2: Đẩy data lên Roboflow để gán nhãn 
---
Step 3: Transformation Data: 9 loại (chia làm 3 lần transform vì gói free): 
Save từng lần xuống dưới local
---
[đầu năm 2025] Step 4: Đẩy ngược 4500 tấm lên Roboflow. 
Thư mục push lên: 

```
Đây là một cửa sổ thông báo từ một công cụ dùng để gắn nhãn (annotation) hình ảnh, thường được sử dụng trong các dự án machine learning hoặc computer vision. Cụ thể:

1. **Zero Area Annotations**: Hệ thống tự động loại bỏ các nhãn (annotations) có diện tích bằng 0 (không chứa bất kỳ pixel nào). Những nhãn này không có giá trị cho việc huấn luyện mô hình.

2. **Trimmed Annotations**: Các nhãn được cắt bớt để đảm bảo chúng nằm hoàn toàn trong khung hình ảnh. Điều này giúp tránh các lỗi khi nhãn vượt ra ngoài phạm vi của bức ảnh.

3. **Affected Files**: Đây là danh sách các file hình ảnh bị ảnh hưởng bởi các chỉnh sửa trên (như s247.jpg, s270.jpg, v.v.).

Nút "Continue" cho phép bạn tiếp tục sau khi hệ thống đã thực hiện các thay đổi trên annotations. Công cụ này thường gặp trong các nền tảng như Label Studio, Roboflow hoặc các phần mềm quản lý dữ liệu hình ảnh khác.
```