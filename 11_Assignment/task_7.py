# Melakukan Image Brightening

import cv2
import numpy as np

image = cv2.imread('haerin.jpg')

getAlpha = 2.5
getBeta = 10


adjustBrightness = cv2.convertScaleAbs(image, alpha=getAlpha, beta=getBeta)

cv2.imshow("Haerin", adjustBrightness)
cv2.imwrite("./out_file/Task_7_brightness_image.jpg", adjustBrightness)
cv2.waitKey()
