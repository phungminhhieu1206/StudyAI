import cv2 as cv
from matplotlib import pyplot as plt

# 0. Load ảnh
image = cv.imread('C:\\Users\\phung\\Desktop\\dataset_entry_test\\image.png')
(h, w, d) = image.shape
cv.imshow('Image_1', image)
cv.waitKey(0)

# 1. Cắt góc phần tư phía trên bên trái
# img_14 = image[0:int(h / 2), 0:int(w / 2)]
# cv.imshow('Image_2', img_14)
# cv.waitKey(0)

# 2. Resize ảnh, dài rộng còn một nửa
# dim = (int(w / 2), int(h / 2))
# img_resized = cv.resize(image, dim)
# cv.imshow('Image_3', img_resized)
# cv.waitKey(0)


# 3. Thực hiện Gaussian blur ảnh
# Load and blur image
blur = cv.GaussianBlur(image, (5, 5), 0)

# Convert color from bgr (OpenCV default) to rgb
img_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

# Display
plt.subplot(221), plt.imshow(img_rgb), plt.title('Gauss Noise')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur_rgb), plt.title('Gauss Noise - Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


# 4. Phát hiện edge trong ảnh
def canny_edge_detection(img, blur_ksize=5, threshold1=100, threshold2=200):
    """
    image_path: link to image
    blur_ksize: Gaussian kernel size
    threshold1: min threshold
    threshold2: max threshold
    """
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_gaussian = cv.GaussianBlur(gray, (blur_ksize, blur_ksize), 0)

    img_canny = cv.Canny(img_gaussian, threshold1, threshold2)

    return img_canny

# img_canny1 = canny_edge_detection(image)
# cv.imshow('Image_4', img_canny1)
# cv.waitKey(0)
