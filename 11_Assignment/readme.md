# THIS IS ASSIGNMENT TASK

1.  Menampilkan Citra

2.  Mengubah Citra warna menjadi Citra Grayscale dan Citra Biner

3.  Memperlihatkan pixel-pixel dalam Citra

4.  Membuat Citra Negatif

5.  Menampilkan Histogram citra

6.  Menampilkan Ekualisasi Citra

7.  Melakukan Image Brightening

8.  Melakukan Operasi Aritmatika dua buah Citra

9.  Melakukan Operasi Boolean

10. Melakukan Operasi Geometri (translasi, rotasi, flipping, zooming)

11. Melakukan proses Image Filtering

============================================================================

JIKA TERDAPAT ERROR WARNING :

> [ WARN:0@0.029] global loadsave.cpp:248 cv::findDecoder imread\_('haerin.jpg'): can't open/read file: check file path/integrity

DAPAT GUNAKAN Module Requests

> ini Adalah contoh pada Soal 1

```python

import cv2
import requests

response = requests.get(url)
url = 'https://cdns.klimg.com/resized/630x/g/d/i/dijuluki_sebagai_pemilik_fairy_voice_intip_8_potret_swag_haerin_newjeans/haerin_newjeans-20230725-002-non_fotografer_kly.jpg'


with open('gambar.jpg', 'wb') as file:
     file.write(response.content)

image = cv2.imread('gambar.jpg')

cv2.imshow("haerin", image)
cv2.waitKey()

```