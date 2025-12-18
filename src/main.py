import os
from utils import load_image, show_image


def main():
    image_path = os.path.join("data", "sample_qr.jpg")
    print("--- BẮT ĐẦU CHƯƠNG TRÌNH ---")
    original_img = load_image(image_path)
    if original_img is not None:
        show_image("Anh Goc (Original)", original_img)
    else:
        print("Dừng chương trình do lỗi đọc ảnh.")


if __name__ == "__main__":
    main()
