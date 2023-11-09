import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
image = cv2.imread('haerin.jpg')

blur_1 = cv2.blur(image, (5, 5))

formula_window = np.zeros((100, 800, 3), dtype=np.uint8)


cv2.putText(formula_window, 'Rumus Filter Rata-rata: 1/(k*k) * [1 1 1 ... 1]', (
    10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
cv2.putText(formula_window, 'Di sini k = 5, sehingga 1/25 * [1 1 1 1 1', (
    10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
cv2.putText(formula_window, '1 1 1 1 1    1 1 1 1 1', (10, 90),
            cv2.FONT_ITALIC, 0.8, (255, 255, 255), 2)
cv2.imshow('Formula', formula_window)

cv2.imshow('Original Image', image)
cv2.imshow('Image blurred', blur_1)
cv2.waitKey(0)
