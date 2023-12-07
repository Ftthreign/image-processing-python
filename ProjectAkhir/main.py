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

# Membaca gambar
image = cv2.imread('./Gambar/Sampel_1.jpg')
resized_image = cv2.resize(image, None, fx=0.2, fy=0.2)
# Mengonversi gambar ke dalam skala abu-abu
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
# Mengaburkan gambar untuk mengurangi noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)
# Mendeteksi tepi menggunakan metode Canny
edges = cv2.Canny(blur, 50, 150)

# Menampilkan hasil
cv2.imshow('Original Image', resized_image)
cv2.imshow("Canny Edge", edges)
cv2.waitKey()
cv2.destroyAllWindows()
