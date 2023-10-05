import cv2
import matplotlib.pyplot as plt

image = cv2.imread('haerin.jpg')


def equalize_image(image):
    get_imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(get_imageRGB)

    r_equalization = cv2.equalizeHist(r)
    g_equalization = cv2.equalizeHist(g)
    b_equalization = cv2.equalizeHist(b)

    get_equalization = cv2.merge(
        (r_equalization, g_equalization, b_equalization))

    return get_equalization


def get_histogram(image):
    get_imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(get_imageRGB)

    r_histogram = cv2.calcHist([r], [0], None, [256], [0, 256])
    g_histogram = cv2.calcHist([g], [0], None, [256], [0, 256])
    b_histogram = cv2.calcHist([b], [0], None, [256], [0, 256])

    plt.figure(figsize=(10, 5))
    plt.subplot(131)
    plt.title('Red Channel Histogram')
    plt.plot(r_histogram, color='red')

    plt.subplot(132)
    plt.title('Green Channel Histogram')
    plt.plot(g_histogram, color='green')

    plt.subplot(133)
    plt.title('Blue Channel Histogram')
    plt.plot(b_histogram, color='blue')

    plt.tight_layout()
    plt.show()


get_histogram(equalize_image(image))
