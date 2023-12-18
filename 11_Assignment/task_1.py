# Menampilkan citra
import cv2

image = cv2.imread('haerin.jpg')
resized = cv2.resize(image, None, fx=0.75, fy=0.75)


cv2.imshow("haerin", resized)
cv2.waitKey()
