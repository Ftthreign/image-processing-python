import cv2

image = cv2.imread('haerin.jpg')

negative_image = 255 - image


cv2.imwrite('./out_file/task_4.jpg', negative_image)
cv2.imshow("gambar Negatif", negative_image)
cv2.waitKey()
