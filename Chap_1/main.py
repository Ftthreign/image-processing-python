import cv2
import numpy as np

# Baca gambar
image = cv2.imread('hyerin.jpeg')

get_r = image[:,:,0]
get_g = image[:,:,1]
get_b = image[:,:,2]

get_row = len(image)
get_col = len(image[0])

scaling_factor = 0.5  


resized_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor)

img_grey = np.zeros((get_row, get_col), dtype=np.uint8)
for row in range(get_row):
    for col in range(get_col):
        img_grey[row, col] = round(0.299 * get_b[row, col] + 0.587 * get_g[row, col] + 0.114 * get_r[row, col])


np.savetxt('get_matrixes.txt', img_grey, fmt='%d', delimiter='\t')

cv2.imshow('hyerin', resized_image)
cv2.waitKey()
