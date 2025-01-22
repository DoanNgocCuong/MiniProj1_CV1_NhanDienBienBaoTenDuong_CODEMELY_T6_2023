import os
import re

# Thay đổi đường dẫn tới thư mục chứa các file ảnh của bạn
folder_path = r'D:\OneDrive - Hanoi University of Science and Technology\ITE10 - Data Science and AI - HUST\Data for Github\Data Sign Recognition Proj'
folder_path = r'D:\OneDrive - codemely\Data_MiniProject\Biển_tên_đường'

# Định dạng mới cho các tập tin ảnh của bạn
new_name_format = 's{}.jpg'

# Lấy danh sách tất cả các tệp tin trong thư mục
file_list = os.listdir(folder_path)

# Biến đếm để định dạng tên mới
count = 1

# Duyệt qua từng file trong thư mục
for file_name in file_list:
    # Kiểm tra nếu tệp tin là ảnh (theo phần mở rộng)
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png') or file_name.endswith('.PNG') or file_name.endswith('.jfif') or file_name.endswith('.gif'):
        # Tạo tên mới cho file ảnh
        new_file_name = new_name_format.format(count)
        
        # Đường dẫn ban đầu của file ảnh
        old_file_path = os.path.join(folder_path, file_name)
        
        # Đường dẫn mới của file ảnh
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # Thực hiện đổi tên file
        os.rename(old_file_path, new_file_path)
        
        # Tăng biến đếm
        count += 1

