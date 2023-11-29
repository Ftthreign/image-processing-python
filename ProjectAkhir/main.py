# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# image = cv2.imread('./mobil.jpeg')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur_image = cv2.GaussianBlur(gray_image, (11, 11), 0)

# canny_image = cv2.Canny(blur_image, 30, 150, 3)

# dilated_image = cv2.dilate(canny_image, (1, 1), iterations=0)

# (cnt, hierarchy) = cv2.findContours(
#     dilated_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.drawContours(rgb_image, cnt, -1, (0, 255, 0), 2)
# print(f"Jumlah mobil dalam gambar : {len(cnt)}")

# plt.imshow(rgb_image)
# plt.axis('off')
# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./mobil.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image, (11, 11), 0)
canny_image = cv2.Canny(blur_image, 30, 150, 3)
dilated_image = cv2.dilate(canny_image, (1, 1), iterations=0)

(cnt, hierarchy) = cv2.findContours(
    dilated_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

car_count = 0

for c in cnt:
    x, y, w, h = cv2.boundingRect(c)

    if w >= 39 and h >= 39:
        cv2.rectangle(rgb_image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        car_count += 1

print(f"Jumlah mobil dalam gambar : {car_count}")

plt.imshow(rgb_image)
plt.axis('off')
plt.show()
