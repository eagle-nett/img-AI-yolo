# Phân loại ảnh theo đặc trưng
  Tự động quét một thư mục ảnh → Phân loại ảnh có chứa người hoặc sản phẩm (theo nhãn YOLOv8) → Lưu vào thư mục riêng biệt.
  
  Nếu ảnh lỗi không xử lý được thì ghi vào file log (errors.txt). Cuối cùng in và lưu tổng kết quá trình chạy.

## Kết quả sau khi chạy:
Ảnh được chia làm 2 nhóm: has và no

Ảnh lỗi (nếu có) được ghi lại trong errors.txt

Tóm tắt được lưu vào summary.txt
## thư viện
  pip install ultralytics opencv-python

  python -m ensurepip
