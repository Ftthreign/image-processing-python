# Mengubah Citra warna menjadi citra grayscale dan citra biner

import cv2
import numpy as np


image = cv2.imread('haerin.jpg')


grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)[1]

get_matrixes_binary = np.array(binary_image)
get_matrixes_grayscale = np.array(grayscale_image)

print(
    f'Grayscale image matrixes :\n{get_matrixes_grayscale.flatten()[:100]}\n\n')
print(f'Binary image matrixes : \n {get_matrixes_binary.flatten()[:100]}')

cv2.imwrite('./out_file/grayscaleImage_TASK_2.jpg', grayscale_image)
cv2.imwrite('./out_file/BinaryImage_TASK_2.jpg', binary_image)

cv2.imshow("Grayscale Image", grayscale_image)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
