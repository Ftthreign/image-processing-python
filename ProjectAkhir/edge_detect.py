import cv2
import numpy as np
import matplotlib.pyplot as plt

# Melakukan deteksi tepi dengan metode Canny dan Sobel


def edge_detection_canny(image):
    # Konversi ke gambar grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Deteksi tepi menggunakan metode Canny
    edges = cv2.Canny(gray_image, 50, 150)

    return edges


def edge_detection_sobel(image):
    # Konversi ke gambar grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Sobel gradient
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Magnitudo gradien dan arahnya
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    magnitude = np.uint8(magnitude)

    return magnitude


if __name__ == "__main__":
    # Membaca gambar
    image_path = './Gambar/Sampel_2.jpg'
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, None, fx=0.25, fy=0.25)

    # Deteksi tepi menggunakan metode Canny
    canny_edges = edge_detection_canny(resized_image)

    # Deteksi tepi menggunakan metode Sobel
    sobel_edges = edge_detection_sobel(resized_image)

    # Menampilkan hasil dengan Matplotlib
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Hasil deteksi tepi Canny
    axes[0].imshow(canny_edges, cmap='gray')
    axes[0].set_title('Canny Edge Detection')
    axes[0].axis('off')

    # Hasil deteksi tepi Sobel
    axes[1].imshow(sobel_edges, cmap='gray')
    axes[1].set_title('Sobel Edge Detection')
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()
