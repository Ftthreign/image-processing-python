import cv2
import numpy as np
import matplotlib.pyplot as plt

# Metode template matching
img = cv2.imread('./Gambar/Sampel_8.jpg', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img2 = img.copy()
template = cv2.imread('./Gambar/Mobil_8.jpg', cv2.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# cv2.TM_CCOEFF: Koeffisien korelasi.
# cv2.TM_CCOEFF_NORMED: Koeffisien korelasi ternormalisasi.
# cv2.TM_CCORR: Kross korelasi.
# cv2.TM_CCORR_NORMED: Kross korelasi ternormalisasi.
# cv2.TM_SQDIFF: Perbedaan kuadrat terkecil.
# cv2.TM_SQDIFF_NORMED: Perbedaan kuadrat terkecil ternormalisasi.

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Menerapkan Pencocokan Dengan Template
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Jika metodenya TM_SQDIFF atau TM_SQDIFF_NORMED, ambil minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title(f'Matching Result {meth}'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title(f'Detected Point {meth}'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
