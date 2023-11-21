import cv2
import numpy as np

image1 = cv2.imread('kacamata.jpg')
image2 = cv2.imread('haerin.jpg')

if image1.shape == image2.shape:
    getInput = str(input("Masukkan operasi : "))

    if getInput == 'penjumlahan':
        result = cv2.add(image1, image2)
    elif getInput == 'pengurangan':
        result = cv2.subtract(image1, image2)
    elif getInput == 'perkalian':
        result = cv2.multiply(image1, image2)
    elif getInput == 'pembagian':
        result = cv2.divide(image1, image2)
    else:
        result = None

    get_b = result[:, :, 0]
    get_g = result[:, :, 1]
    get_r = result[:, :, 2]

    get_row = len(result)
    get_col = len(result[0])

    np.set_printoptions(threshold=np.inf)

    for i in range(get_row):
        for j in range(get_col):
            result[i, j] = round(0.299 * get_r[i, j] +
                                 0.587 * get_g[i, j] + 0.114 * get_b[i, j])

    x1, x2 = 10, 30
    y1, y2 = 10, 30

    print(result.flatten()[:100])

    cv2.imshow('Hasil Operasi Aritmatika', result)
    cv2.waitKey(0)

    # print(result[x1:x2, y1:y2])

else:
    print("Citra-citra harus memiliki ukuran yang sama")
