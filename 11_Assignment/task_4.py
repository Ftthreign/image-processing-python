# Membuat Citra negatif

import cv2

image = cv2.imread('haerin.jpg')
resized = cv2.resize(image, None, fx=0.5, fy=0.5)

negative_image = 255 - resized


cv2.imwrite('./out_file/task_4.jpg', negative_image)
cv2.imshow("gambar Negatif", negative_image)
cv2.waitKey()
