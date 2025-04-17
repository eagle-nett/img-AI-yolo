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

## ĐẶC TRƯNG
['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 
'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 
'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 
'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 
'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 
'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 
'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 
'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 
'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 
'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 
'hair drier', 'toothbrush']
