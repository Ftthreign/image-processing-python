import cv2
import numpy as np

# Read Image
image = cv2.imread('HAERIN.jpeg')

# Get RGB Value
get_b = image[:, :, 0]
get_g = image[:, :, 1]
get_r = image[:, :, 2]

# Get column and row from image
get_row = len(image)
get_col = len(image[0])

# Get image window to 0.5x from original size
scaling_factor = 0.5
resized_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor)

# Convert image to Grayscale
img_grey = np.zeros((get_row, get_col), dtype=np.uint8)

# loop to get Matrixes point
for row in range(get_row):
    for col in range(get_col):
        img_grey[row, col] = round(
            0.299 * get_r[row, col] + 0.587 * get_g[row, col] + 0.114 * get_b[row, col])


# Save all matrix info to txt file
np.savetxt('get_matrixes.txt', img_grey, fmt='%d', delimiter='\t')

# Show image window with 0.5x original size
cv2.imshow('hyerin', resized_image)
cv2.waitKey()
