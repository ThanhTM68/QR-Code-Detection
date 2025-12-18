import cv2
import os


def load_image(image_path):
    if not os.path.exists(image_path):
        print(f"Lỗi: Không tìm thấy file tại {image_path}")
        return None
    image = cv2.imread(image_path)
    if image is None:
        print(f"Lỗi: Không thể đọc định dạng file này.")
        return None
    print(f"Đã đọc ảnh thành công: {image.shape}")
    return image


def show_image(title, image, wait_key=0):
    if image is None:
        print("Lỗi: Ảnh rỗng, không thể hiển thị.")
        return

    h, w = image.shape[:2]
    max_width = 1000
    if w > max_width:
        scale = max_width / w
        new_w = max_width
        new_h = int(h * scale)
        display_img = cv2.resize(image, (new_w, new_h))
    else:
        display_img = image
    cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(title, display_img)
    cv2.moveWindow(title, 0, 50)
    cv2.waitKey(wait_key)
    if wait_key == 0:
        cv2.destroyAllWindows()
