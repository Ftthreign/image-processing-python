import cv2
import matplotlib.pyplot as plt

image = cv2.imread('haerin.jpg')

color = ('b', 'g', 'r')

for i, column in enumerate(color):
    getHist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(getHist, color=column)
    plt.xlim([0, 256])

plt.show()
