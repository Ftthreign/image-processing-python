import cv2

image = cv2.imread('haerin.jpg')


grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('./out_file/grayscaleImage_TASK_2.jpg', grayscale_image)

cv2.imshow("Grayscale Image", grayscale_image)
cv2.waitKey()
