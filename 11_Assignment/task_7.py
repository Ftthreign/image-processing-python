# Melakukan Image Brightening

import cv2
import numpy as np

image = cv2.imread('haerin.jpg')
resized = cv2.resize(image, None, fx=0.5, fy=0.5)

getAlpha = 2.5
getBeta = 10

adjustBrightness = cv2.convertScaleAbs(resized, alpha=getAlpha, beta=getBeta)

cv2.imshow("Haerin", adjustBrightness)
cv2.imwrite("./out_file/Task_7_brightness_image.jpg", adjustBrightness)
cv2.waitKey()
