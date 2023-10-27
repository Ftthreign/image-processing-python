import cv2
import numpy as np


image = cv2.imread('haerin.jpg')

get_b = image[:, :, 0]
get_g = image[:, :, 1]
get_r = image[:, :, 2]

get_row = len(image)
get_col = len(image[0])

np.set_printoptions(threshold=np.inf)

img_grey = np.zeros((get_row, get_col), dtype=np.uint8)

for i in range(get_row):
    for j in range(get_col):
        img_grey[i, j] = round(0.299 * get_r[i, j] +
                               0.587 * get_g[i, j] + 0.114 * get_b[i, j])

x1, x2 = 10, 30
y1, y2 = 10, 30

# print(img_grey.flatten()[:100])
print(img_grey[x1:x2, y1:y2])
