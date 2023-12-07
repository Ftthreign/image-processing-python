# Menampilkan Semua (Metode Canny dan Sobel)

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Fungsi Metode Edge Detection
# def edge_detection_canny(image):
#     # Konversi ke gambar grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Deteksi tepi menggunakan metode Canny
#     edges = cv2.Canny(gray_image, 50, 150)

#     return edges

# # Fungsi Metode Sonel Detection
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
#     # Perulangan Untuk Menampilkan Semua Gambar (Sampel 1-10)
#     for i in range(1, 11):
#         image_path = f'./Gambar/Sampel_{i}.jpg'
#         image = cv2.imread(image_path)

#         # Deteksi tepi menggunakan metode Canny
#         canny_edges = edge_detection_canny(image)

#         # Deteksi tepi menggunakan metode Sobel
#         sobel_edges = edge_detection_sobel(image)

#         # Menampilkan hasil dengan Matplotlib
#         fig, axes = plt.subplots(1, 3, figsize=(15, 5))

#         # Hasil deteksi tepi Canny
#         axes[0].imshow(canny_edges, cmap='gray')
#         axes[0].set_title(f'Canny Edge Detection - Sampel {i}')
#         axes[0].axis('off')

#         # Hasil deteksi tepi Sobel
#         axes[1].imshow(sobel_edges, cmap='gray')
#         axes[1].set_title(f'Sobel Edge Detection - Sampel {i}')
#         axes[1].axis('off')

#         # Gambar asli
#         axes[2].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#         axes[2].set_title(f'Original Image - Sampel {i}')
#         axes[2].axis('off')

#         plt.tight_layout()
#         plt.show()


# Menampilkan Manual (Metode Canny dan Sobel)

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Fungsi Metode Edge Detection
# def edge_detection_canny(image):
#     # Konversi ke gambar grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Deteksi tepi menggunakan metode Canny
#     edges = cv2.Canny(gray_image, 50, 150)

#     return edges

# # Fungsi Metode Sobel Detection
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
#     image_path = './Gambar/Sampel_1.jpg'
#     image = cv2.imread(image_path)
#     resized_image = cv2.resize(image, None, fx=0.25, fy=0.25)

#     # Deteksi tepi menggunakan metode Canny
#     canny_edges = edge_detection_canny(resized_image)

#     # Deteksi tepi menggunakan metode Sobel
#     sobel_edges = edge_detection_sobel(resized_image)

#     # Menampilkan hasil dengan Matplotlib
#     fig, axes = plt.subplots(1, 3, figsize=(15, 5))

#     # Hasil deteksi tepi Canny
#     axes[0].imshow(canny_edges, cmap='gray')
#     axes[0].set_title('Canny Edge Detection')
#     axes[0].axis('off')

#     # Hasil deteksi tepi Sobel
#     axes[1].imshow(sobel_edges, cmap='gray')
#     axes[1].set_title('Sobel Edge Detection')
#     axes[1].axis('off')

#     # Gambar asli
#     axes[2].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     axes[2].set_title('Original Image')
#     axes[2].axis('off')

#     plt.tight_layout()
#     plt.show()


# Metode Sobel

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Membaca gambar
# image = cv2.imread('./Gambar/Sampel_7.jpg')
# resized_image = cv2.resize(image, None, fx=0.25, fy=0.25)

# # Mengonversi ke gambar grayscale
# grayScaleImage = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# # Menentukan kernel Robert
# robert_x = np.array([[1, 0], [0, -1]])
# robert_y = np.array([[0, 1], [-1, 0]])

# # Menggunakan filter Robert
# robert_x_filter = cv2.filter2D(grayScaleImage, -1, robert_x)
# robert_y_filter = cv2.filter2D(grayScaleImage, -1, robert_y)

# # Menggabungkan hasil filter Robert untuk mendapatkan tepi
# robert_combined = cv2.bitwise_or(cv2.convertScaleAbs(
#     robert_x_filter), cv2.convertScaleAbs(robert_y_filter))

# # Menampilkan hasil dengan Matplotlib
# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# # Hasil filter Robert
# axes[0].imshow(robert_combined, cmap='gray')
# axes[0].set_title('Robert Edge Detection')
# axes[0].axis('off')

# # Gambar asli
# axes[1].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# axes[1].set_title('Original Image')
# axes[1].axis('off')

# plt.tight_layout()
# plt.show()


# Metode template matching

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar dan Menkonversi Kedalam Grayscale
img = cv.imread('./Gambar/Sampel_8.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img2 = img.copy()
template = cv.imread('./Gambar/Mobil_8.jpg', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]

# Perbandingan Menggunakan 6 Methode Template 
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# cv.TM_CCOEFF: Koeffisien korelasi.
# cv.TM_CCOEFF_NORMED: Koeffisien korelasi ternormalisasi.
# cv.TM_CCORR: Kross korelasi.
# cv.TM_CCORR_NORMED: Kross korelasi ternormalisasi.
# cv.TM_SQDIFF: Perbedaan kuadrat terkecil.
# cv.TM_SQDIFF_NORMED: Perbedaan kuadrat terkecil ternormalisasi.

for meth in methods:
    img = img2.copy()
    method = eval(meth)
    
    # Menerapkan Pencocokan Dengan Template
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    
    # Jika metodenya TM_SQDIFF atau TM_SQDIFF_NORMED, ambil minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()