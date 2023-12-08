import cv2
import numpy as np
import matplotlib.pyplot as plt

# # Melakukan Adaptive Thresholding
# for i in range(1, 11):
#     image = cv2.imread(f'./Gambar/Sampel_{i}.jpg', 0)
#     resize = cv2.resize(image, None, fx=0.25, fy=0.25)

#     # Metode Adaptive Thresholding
#     adaptive_threshold = cv2.adaptiveThreshold(
#         resize, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

#     # Menampilkan hasil thresholding
#     plt.figure(figsize=(8, 4))

#     plt.subplot(121)
#     plt.title('Original')
#     plt.imshow(resize, cmap='gray')
#     plt.axis('off')

#     plt.subplot(122)
#     plt.title(f'Adaptive Thresholding ke-{i}')
#     plt.imshow(adaptive_threshold, cmap='gray')
#     plt.axis('off')

#     plt.tight_layout()
#     plt.show()

# Melakukan deteksi tepi dengan metode Canny dan Sobel


# def edge_detection_canny(image):
#     # Konversi ke gambar grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Deteksi tepi menggunakan metode Canny
#     edges = cv2.Canny(gray_image, 50, 150)

#     return edges


# def edge_detection_sobel(image):
#     # Konversi ke gambar grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Sobel gradient
#     sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
#     sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

#     # Magnitudo gradien dan arahnya
#     magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
#     magnitude = np.uint8(magnitude)

#     return magnitude


# if __name__ == "__main__":
#     # Membaca gambar
#     image_path = './Gambar/Sampel_2.jpg'
#     image = cv2.imread(image_path)
#     resized_image = cv2.resize(image, None, fx=0.25, fy=0.25)

#     # Deteksi tepi menggunakan metode Canny
#     canny_edges = edge_detection_canny(resized_image)

#     # Deteksi tepi menggunakan metode Sobel
#     sobel_edges = edge_detection_sobel(resized_image)

#     # Menampilkan hasil dengan Matplotlib
#     fig, axes = plt.subplots(1, 2, figsize=(15, 5))

#     # Hasil deteksi tepi Canny
#     axes[0].imshow(canny_edges, cmap='gray')
#     axes[0].set_title('Canny Edge Detection')
#     axes[0].axis('off')

#     # Hasil deteksi tepi Sobel
#     axes[1].imshow(sobel_edges, cmap='gray')
#     axes[1].set_title('Sobel Edge Detection')
#     axes[1].axis('off')

#     plt.tight_layout()
#     plt.show()


# Metode deteksi Tambahan : Robet
# image = cv2.imread('./Gambar/Sampel_7.jpg')
# resized_image = cv2.resize(image, None, fx=0.25, fy=0.25)
# grayScaleImage = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# robert_x = np.array([[1, 0], [0, -1]])
# robert_y = np.array([[0, 1], [-1, 0]])

# robert_x_filter = cv2.filter2D(grayScaleImage, -1, robert_x)
# robert_y_filter = cv2.filter2D(grayScaleImage, -1, robert_y)

# robert_combined = cv2.bitwise_or(cv2.convertScaleAbs(
#     robert_x_filter), cv2.convertScaleAbs(robert_y_filter))

# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# axes[0].imshow(robert_combined, cmap='gray')
# axes[0].set_title('Robert Edge Detection')
# axes[0].axis('off')

# axes[1].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# axes[1].set_title('Original Image')
# axes[1].axis('off')

# plt.tight_layout()
# plt.show()


# Metode template matching
img = cv2.imread('./Gambar/Sampel_10.jpg', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img2 = img.copy()
template = cv2.imread('./Gambar/Mobil_10.jpg', cv2.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# cv2.TM_CCOEFF: Koeffisien korelasi.
# cv2.TM_CCOEFF_NORMED: Koeffisien korelasi ternormalisasi.
# cv2.TM_CCORR: Kross korelasi.
# cv2.TM_CCORR_NORMED: Kross korelasi ternormalisasi.
# cv2.TM_SQDIFF: Perbedaan kuadrat terkecil.
# cv2.TM_SQDIFF_NORMED: Perbedaan kuadrat terkecil ternormalisasi.

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Menerapkan Pencocokan Dengan Template
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Jika metodenya TM_SQDIFF atau TM_SQDIFF_NORMED, ambil minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title(f'Matching Result {meth}'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title(f'Detected Point {meth}'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
