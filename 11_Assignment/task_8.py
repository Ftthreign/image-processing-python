import cv2
import numpy as np

def operasi_aritmatika(citra1_path, citra2_path, operator):
    # Membaca citra.
    img1 = cv2.imread("1.png")
    img2 = cv2.imread("2.png")

    # Memastikan ukuran citra sama.
    assert img1.shape == img2.shape, "Ukuran citra tidak sama."
    
    
    img1a = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)[1]
    img2a = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)[1]
    
    # Menampilkan matrix img1 dan img2.
    print(f"Matrix img1:\n{img1a}")
    print(f"Matrix img2:\n{img2a}")

    # Melakukan operasi aritmatika.
    if operator == "+":
        img_hasil = cv2.add(img1a, img2a)
    elif operator == "-":
        img_hasil = cv2.subtract(img1a, img2a)
    elif operator == "*":
        img_hasil = cv2.multiply(img1a, img2a)
    elif operator == "/":
        img_hasil = cv2.divide(img1a, img2a)
    else:
        raise ValueError("Operator aritmatika tidak valid.")

    # Menyimpan citra hasil.
    print(img_hasil)

    # Resize image to fit the screen
    cv2.namedWindow("Hasil :", cv2.WINDOW_NORMAL)
    cv2.imshow("Hasil :", img_hasil)
    cv2.waitKey(0)
    cv2.imwrite("hasil.jpg", img_hasil)

    return img_hasil

# Ubah path citra1.jpg dan citra2.jpg sesuai dengan kebutuhan.
pilihan = input("Masukan Pilihan : ")
operasi_aritmatika("citra1.jpg", "citra2.jpg", pilihan)
