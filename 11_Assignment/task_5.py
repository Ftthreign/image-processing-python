# Menampilkan histogram Citra

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('haerin.jpg')

color = ('b', 'g', 'r')
plt.figure(figsize=(10, 5))

for i, column in enumerate(color):
    getHist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.subplot(1, 2, 1)
    plt.plot(getHist, color=column)
    plt.xlim([0, 256])

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
