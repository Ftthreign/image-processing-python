# Melakukan Operasi Boolean

# Senang bisa berkontribusi :D
import cv2


def operation_or(image1, image2):
    if image1.shape == image2.shape:
        hasil = cv2.bitwise_or(image1, image2)
        return hasil
    else:
        print("\nUkuran citra tidak cocok.")
        return None


def operation_and(image1, image2):
    if image1.shape == image2.shape:
        hasil = cv2.bitwise_and(image1, image2)
        return hasil
    else:
        print("\nUkuran citra tidak cocok.")
        return None


def operation_xor(image1, image2):
    if image1.shape == image2.shape:
        hasil = cv2.bitwise_xor(image1, image2)
        return hasil
    else:
        print("\nUkuran citra tidak cocok.")
        return None


img1 = cv2.imread("./Gambar2.jpeg")
img2 = cv2.imread("./Gambar1.jpeg")

if img1 is None or img2 is None:
    print("Tidak dapat membaca citra.")
else:
    print("Operasi:\n1. OR\n2. AND\n3. XOR")
    pil = int(input("Pilih (1/2/3): "))
    if pil == 1:
        result_image = operation_or(img1, img2)
    elif pil == 2:
        result_image = operation_and(img1, img2)
    elif pil == 3:
        result_image = operation_xor(img1, img2)
    else:
        print("\nPilihan tidak valid. Mohon input 1 atau 2 atau 3.")

if result_image is not None:
    cv2.namedWindow("Hasil :", cv2.WINDOW_NORMAL)
    cv2.imshow("Hasil :", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("\n", result_image)
