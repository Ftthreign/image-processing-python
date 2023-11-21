import cv2
# import numpy as np

img1 = cv2.imread('Gambar1.jpeg')
img2 = cv2.imread('Gambar2.jpeg')


if img1.shape == img2.shape:

    img1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)[1]
    img2 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)[1]

    # Menampilkan matrix img1 dan img2.
    print(f"Matrix img1:\n{img1}")
    print(f"Matrix img2:\n{img2}")

    # Melakukan operasi aritmatika.
    operator = str(input("Masukkan Operasi (+, -, *, /) : "))
    if operator == "+":
        img_hasil = cv2.add(img1, img2)
    elif operator == "-":
        img_hasil = cv2.subtract(img1, img2)
    elif operator == "*":
        img_hasil = cv2.multiply(img1, img2)
    elif operator == "/":
        img_hasil = cv2.divide(img1, img2)
    else:
        raise ValueError("Operator aritmatika tidak valid.")

    # Menyimpan citra hasil.
    print(img_hasil)

    # Resize image to fit the screen
    cv2.namedWindow("Hasil :", cv2.WINDOW_NORMAL)
    cv2.imshow("Hasil :", img_hasil)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Citra-citra harus memiliki ukuran yang sama")
