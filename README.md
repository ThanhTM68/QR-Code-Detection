# QR Code Localization System (Hệ thống Định vị Mã QR)

> **Đồ án môn học:** Xử lý ảnh số  
> **Ngôn ngữ:** Python 3 + OpenCV

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

## Giới thiệu (Introduction)

Dự án này là một hệ thống thị giác máy tính (Computer Vision) có khả năng phát hiện và định vị mã QR trong hình ảnh.

Khác với việc sử dụng các thư viện (như `pyzbar`), dự án này tập trung vào việc **xây dựng thuật toán từ gốc** sử dụng các kỹ thuật xử lý ảnh cổ điển (Classical Image Processing) để hiểu sâu về bản chất toán học và hình học của mã QR.

## Tính năng chính (Key Features)

-   [x] Đọc và xử lý ảnh đầu vào từ file.
-   [x] **Tiền xử lý mạnh mẽ:** Chuyển đổi không gian màu, khử nhiễu (Gaussian Blur) và phân ngưỡng thích nghi (Adaptive Thresholding) để hoạt động tốt trong điều kiện ánh sáng không đều.
-   [x] **Phát hiện Finder Pattern:** Sử dụng phân tích đường bao (Contour) và cây phả hệ (Hierarchy) để tìm cấu trúc lồng nhau (Đen-Trắng-Đen) đặc trưng của mã QR.
-   [x] **Sắp xếp hình học:** Xác định hướng và vị trí chính xác của mã QR (Đang phát triển).

## Cấu trúc dự án (Directory Structure)

    QR-Code-Detection/
    ├── data/ # Chứa dữ liệu ảnh (Input)
    │ └── sample_qr.jpg
    ├── src/ # Mã nguồn chương trình (Source Code)
    │ ├── main.py # File chính để chạy chương trình
    │ ├── preprocess.py # Module tiền xử lý ảnh
    │ ├── detection.py # Module phát hiện đặc trưng
    │ └── utils.py # Các hàm tiện ích (I/O, Visualization)
    ├── .gitignore # Cấu hình file bỏ qua của Git
    ├── requirements.txt # Danh sách thư viện Python
    └── README.md # Tài liệu hướng dẫn

## Cài đặt (Installation)

Đảm bảo bạn đã cài đặt Python 3 trên máy tính.

1. **Clone dự án về máy:**

    ```bash
    git clone [https://github.com/username-cua-ban/QR-Code-Detection.git](https://github.com/username-cua-ban/QR-Code-Detection.git)
    cd QR-Code-Detection
    ```

2. **Thiết lập môi trường (Khuyến nghị)**

> Phần này giúp thiết lập môi trường chạy dự án một cách ổn định. Nếu đã quen với Python, bạn có thể bỏ qua môi trường ảo.

### Windows

    ```bash
    python -m venv venv
    venv\Scripts\activate
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
