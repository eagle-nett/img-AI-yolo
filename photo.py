import os
import shutil
import uuid
import time
from datetime import datetime
from ultralytics import YOLO

# Đường dẫn thư mục ảnh gốc và nơi lưu kết quả
SOURCE_DIR = r"C:\tdat\CODE\lọc ảnh_py\images test code"
OUTPUT_HAS_OBJECTS = r"C:\tdat\CODE\lọc ảnh_py\has_objects"
OUTPUT_NO_OBJECTS = r"C:\tdat\CODE\lọc ảnh_py\no_objects"
ERROR_FOLDER = r"C:\tdat\CODE\lọc ảnh_py\errors"  # Thư mục chứa ảnh lỗi
ERROR_LOG = "errors.txt"
SUMMARY_LOG = "summary.txt"

# Tạo thư mục nếu chưa có
os.makedirs(OUTPUT_HAS_OBJECTS, exist_ok=True)
os.makedirs(OUTPUT_NO_OBJECTS, exist_ok=True)
os.makedirs(ERROR_FOLDER, exist_ok=True)  # Tạo thư mục lỗi

# Mô hình YOLO
model = YOLO('yolov8n.pt')

# Định dạng ảnh được hỗ trợ
SUPPORTED = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
images = [f for f in os.listdir(SOURCE_DIR) if f.lower().endswith(SUPPORTED)]

# Xóa file log cũ nếu có
if os.path.exists(ERROR_LOG):
    os.remove(ERROR_LOG)
if os.path.exists(SUMMARY_LOG):
    os.remove(SUMMARY_LOG)

start_time = time.time()
processed = 0
error_count = 0

for idx, file in enumerate(images):
    path = os.path.join(SOURCE_DIR, file)

    try:
        result = model(path, verbose=False)[0]
        labels = [model.names[int(cls)] for cls in result.boxes.cls]

        # Đổi tên file để tránh đè nếu trùng
        name, ext = os.path.splitext(file)
        new_name = f"{name}_{uuid.uuid4().hex[:6]}{ext}"

        # Nếu có người hoặc sản phẩm → copy vào has_objects
        if any(label in ['person', 'backpack', 'handbag', 'bottle', 'tv', 'cell phone', 'book'] for label in labels):
            shutil.copy2(path, os.path.join(OUTPUT_HAS_OBJECTS, new_name))
        else:
            shutil.copy2(path, os.path.join(OUTPUT_NO_OBJECTS, new_name))

        processed += 1

        if idx % 20 == 0 or idx == len(images) - 1:
            print(f"✔ Đã xử lý {idx + 1}/{len(images)} ảnh")

    except Exception as e:
        error_count += 1
        with open(ERROR_LOG, "a", encoding="utf-8") as f:
            f.write(f"{file} - {str(e)}\n")

        # Copy ảnh lỗi vào thư mục errors
        try:
            shutil.copy2(path, os.path.join(ERROR_FOLDER, file))
        except Exception as copy_error:
            # Nếu lỗi luôn cả khi copy thì cũng log ra luôn
            with open(ERROR_LOG, "a", encoding="utf-8") as f:
                f.write(f"{file} - Failed to copy to errors folder: {str(copy_error)}\n")

# Tổng kết
end_time = time.time()
summary = f"""
🗓️  Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📷  Tổng ảnh: {len(images)}
✅  Thành công: {processed}
❌  Lỗi: {error_count}
⏱️  Thời gian chạy: {round(end_time - start_time, 2)} giây
"""

print(summary)
with open(SUMMARY_LOG, "w", encoding="utf-8") as f:
    f.write(summary)
