import cv2
import numpy as np

image = cv2.imread('haerin.jpg')

scaling_factor = 0.5
resized_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor)

rows, cols = resized_image.shape[:2]
height, width = resized_image.shape[:2]

# Scaling / Zooming
result_scaled = cv2.resize(resized_image, (3*height, 2*width),
                           interpolation=cv2.INTER_CUBIC)

# Translation
"""
    FORMULA FOR TRANSLATION
    M = [1, 0, tx], [0,1,ty]

    tx = translation at x coordinat
    ty = translation at y coordinat
"""
M_translate = np.float64([[1, 0, -100], [0, 1, 100]])
result_translate = cv2.warpAffine(resized_image, M_translate, (cols, rows))


# Rotation
"""
    FORMULA FOR ROTATION
    M = [cosθ, -sinθ], [sinθ, cosθ]

"""
M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
result_rotate = cv2.warpAffine(resized_image, M_rotate, (cols, rows))

# Flipping

result_flipped = cv2.flip(resized_image, 1)

cv2.imwrite('./out_file/Scaled_image_task_10.jpg', result_scaled)
cv2.imwrite('./out_file/translated_image_task_10.jpg', result_translate)
cv2.imwrite('./out_file/Rotated_image_task_10.jpg', result_rotate)
cv2.imwrite('./out_file/Flipped_image.jpg', result_flipped)

# result_scaled = cv2.resize(result_scaled, (cols, rows))

# merge_output = np.concatenate(
#     (result_scaled, result_translate, result_rotate, result_flipped))

# cv2.imshow('Combined Image', merge_output)

cv2.imshow('Scaled image', result_scaled)
cv2.imshow('Translated image', result_translate)
cv2.imshow('Rotated image', result_rotate)
cv2.imshow('Flipped image', result_flipped)

cv2.waitKey(0)
