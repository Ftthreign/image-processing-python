# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# image = cv2.imread('./Gambar/Sampel_1.jpg')
# resized_image = cv2.resize(image, None, fx=0.25, fy=0.25)

# # Processing Image
# grayScaleImage = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(grayScaleImage, (5, 5), 0)
# edges = cv2.Canny(blur, 50, 150)
# dilated = cv2.dilate(edges, (1, 1), iterations=0)

# (cnt, hierarchy) = cv2.findContours(
#     dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# rgb = cv2.cvtColor(blur, cv2.COLOR_GRAY2RGB)

# # Membuat gambar hitam dengan ukuran sama
# black_image = np.zeros_like(resized_image)

# for c in cnt:
#     x, y, w, h = cv2.boundingRect(c)
#     if w > 30 and h > 30:
#         cv2.drawContours(black_image, [c], -1, (255, 255, 255), -1)

# cv2.imshow("Contours Image", black_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Baca gambar
image = cv2.imread("./Gambar/Sampel_1.jpg")
resized_image = cv2.resize(image, None, fx=0.20, fy=0.20)
# Konversi ke skala abu-abu
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Deteksi tepi menggunakan metode Canny
edges_canny = cv2.Canny(gray, 50, 150)

# Deteksi tepi menggunakan metode Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
edges_sobel = np.sqrt(sobelx**2 + sobely**2)

adaptive_thres = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imwrite('./Hasil/Sampel_1_Grayscale.jpg', gray)
cv2.imwrite('./Hasil/Sampel_1_Canny.jpg', edges_canny)
cv2.imwrite('./Hasil/Sampel_1_Sobel.jpg', edges_sobel)

# cv2.imshow("Grayscale Image", gray)
cv2.imshow('Threshold', adaptive_thres)
# cv2.imshow("Canny Edge Detection", edges_canny)
# cv2.imshow("Sobel Edge Detection", edges_sobel.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()
