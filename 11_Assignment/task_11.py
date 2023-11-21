# Melakukan proses Image Filtering

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('haerin.jpg')

# formula_window = np.zeros((100, 800, 3), dtype=np.uint8)
# cv2.putText(formula_window, 'Rumus Filter Rata-rata: 1/(k*k) * [1 1 1 ... 1]', (
#     10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
# cv2.putText(formula_window, 'Di sini k = 5, sehingga 1/25 * [1 1 1 1 1', (
#     10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
# cv2.putText(formula_window, '1 1 1 1 1    1 1 1 1 1', (10, 90),
#             cv2.FONT_ITALIC, 0.8, (255, 255, 255), 2)
# cv2.imshow('Formula', formula_window)

print('1. Filter blur biasa')
print('2. filter linear : averaging')
print('3. filter non-linear median blur')

input = int(input("Masukkan nilai : "))

if input == 1:
    # blur image
    blur = cv2.blur(image, (5, 5))
    result = np.hstack((image, blur))
    print(blur.flatten()[:50])
elif input == 2:
    # averaging image (linear filtering)
    set_kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(image, -1, kernel=set_kernel)
    result = np.hstack((image, dst))
    print(dst.flatten()[:50])
elif input == 3:
    # median image (non-linear filtering)
    median = cv2.medianBlur(image, 5)
    result = np.hstack((image, median))
    print(median.flatten()[:50])

cv2.imshow('Haerin', result)
cv2.waitKey(0)
