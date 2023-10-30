import cv2
import numpy as np

# Baca gambar
img = cv2.imread('haerin.jpg')

# Buat kernel filter rata-rata
kernel = np.ones((5, 5), np.float32) / 25

# Terapkan filter rata-rata menggunakan fungsi filter2D
output = cv2.filter2D(img, -1, kernel)

# Tampilkan gambar asli dan gambar hasil filtering
cv2.imshow('Gambar Asli', img)
cv2.imshow('Hasil Filtering', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
