# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# image = cv2.imread('./Gambar/Sampel_2.jpg')
# resized_image = cv2.resize(image, None, fx=0.25, fy=0.25)

# # Processing Image
# grayScaleImage = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(grayScaleImage, (5, 5), 0)
# edges = cv2.Canny(blur, 50, 150)
# dilated = cv2.dilate(edges, (1, 1), iterations=0)

# (cnt, hierarchy) = cv2.findContours(
#     dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# rgb = cv2.cvtColor(blur, cv2.COLOR_GRAY2RGB)

# # Membuat gambar hitam dengan ukuran yang sama
# black_image = np.zeros_like(resized_image)

# for c in cnt:
#     x, y, w, h = cv2.boundingRect(c)
#     if w > 30 and h > 30:
#         cv2.drawContours(black_image, [c], -1, (255, 255, 255), -1)

# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# # Gambar asli
# axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# axes[0].set_title('Original Image')

# # Hasil proses
# axes[1].imshow(cv2.cvtColor(black_image, cv2.COLOR_BGR2RGB))
# axes[1].set_title('Processed Image')
# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
image = cv2.imread('./Gambar/Sampel_1.jpg')
resized_image = cv2.resize(image, None, fx=0.25, fy=0.25)

# Mengonversi ke gambar grayscale
grayScaleImage = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Menentukan kernel Robert
robert_x = np.array([[1, 0], [0, -1]])
robert_y = np.array([[0, 1], [-1, 0]])

# Menggunakan filter Robert
robert_x_filter = cv2.filter2D(grayScaleImage, -1, robert_x)
robert_y_filter = cv2.filter2D(grayScaleImage, -1, robert_y)

# Menggabungkan hasil filter Robert untuk mendapatkan tepi
robert_combined = cv2.bitwise_or(cv2.convertScaleAbs(
    robert_x_filter), cv2.convertScaleAbs(robert_y_filter))

# Menampilkan hasil dengan Matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Hasil filter Robert
axes[0].imshow(robert_combined, cmap='gray')
axes[0].set_title('Robert Edge Detection')
axes[0].axis('off')

# Gambar asli
axes[1].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[1].set_title('Original Image')
axes[1].axis('off')

plt.tight_layout()
plt.show()
