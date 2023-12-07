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
# # cv2.imshow("Original Image", resized_image)
# # cv2.imshow("Edge Detection", edges)
# # cv2.imshow("Dilation", dilated)
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

# Deteksi tepi menggunakan metode Prewitt
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewittx = cv2.filter2D(gray, -1, kernelx)
prewitty = cv2.filter2D(gray, -1, kernely)
edges_prewitt = np.sqrt(prewittx**2 + prewitty**2)

# Tampilkan hasil
cv2.imshow("Original Image", resized_image)
cv2.imshow("Canny Edge Detection", edges_canny)
cv2.imshow("Sobel Edge Detection", edges_sobel.astype(np.uint8))
cv2.imshow("Prewitt Edge Detection", edges_prewitt.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
