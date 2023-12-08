import cv2
import matplotlib.pyplot as plt

# Melakukan Adaptive Thresholding
for i in range(1, 11):
    image = cv2.imread(f'./Gambar/Sampel_{i}.jpg', 0)
    resize = cv2.resize(image, None, fx=0.25, fy=0.25)

    # Metode Adaptive Thresholding
    adaptive_threshold = cv2.adaptiveThreshold(
        resize, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Menampilkan hasil thresholding
    plt.figure(figsize=(8, 4))

    plt.subplot(121)
    plt.title('Original')
    plt.imshow(resize, cmap='gray')
    plt.axis('off')

    plt.subplot(122)
    plt.title(f'Adaptive Thresholding ke-{i}')
    plt.imshow(adaptive_threshold, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
