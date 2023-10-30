import cv2
import numpy as np

# Baca dua citra
image1 = cv2.imread('kacamata.jpg')
image2 = cv2.imread('haerin.jpg')

# Pastikan citra memiliki ukuran yang sama
if image1.shape == image2.shape:
    # Lakukan operasi aritmatika, contoh: pengurangan
    result = cv2.subtract(image1, image2)

    # Tampilkan citra hasil
    cv2.imshow('Hasil Operasi Aritmatika', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Citra-citra harus memiliki ukuran yang sama")