import cv2
import numpy as np


image = cv2.imread('haerin.jpg')

get_b = image[:, :, 0]
get_g = image[:, :, 1]
get_r = image[:, :, 2]

get_row = len(image)
get_col = len(image[0])

img_grey = np.zeros((get_row, get_col), dtype=np.uint8)

for i in range(get_row):
    for j in range(get_col):
        img_grey[i, j] = round(0.299 * get_r[i, j] +
                               0.587 * get_g[i, j] + 0.114 * get_b[i, j])

print(img_grey)
