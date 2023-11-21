# Menampilkan ekualisasi Citra

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('haerin.jpg')


def get_r(image):
    histogram, bins = np.histogram(image.flatten(), 256, [0, 256])

    cdf = histogram.cumsum()
    cdf_normalisasi = cdf * float(histogram.max()) / cdf.max()

    plt.plot(cdf_normalisasi, color='b')
    plt.hist(image.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper right')
    plt.show()


def get_equalized_image(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(grayscale)
    result = np.hstack((grayscale, equ))
    cv2.imshow('gambar', result)
    cv2.waitKey(0)


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
    plt.subplot(133)
    plt.plot(r_histogram, color='red')

    plt.subplot(132)
    plt.plot(g_histogram, color='green')

    plt.subplot(131)
    plt.plot(b_histogram, color='blue')

    plt.savefig('./out_file/hasil_task_6.jpg', format='jpg')
    plt.tight_layout()
    plt.show()


print("1. Equalisasi semua RGB citra dan tampilkan histogram")
print("2. Equalisasi pixel Red pada citra dan tampilkan histogram")
print("3. Tampilkan hasil equalisasi citra")

input = int(input("Masukkan pilihan : "))
match input:
    case 1:
        get_histogram(equalize_image(image))
    case 2:
        get_r(image)
    case 3:
        get_equalized_image(image)
