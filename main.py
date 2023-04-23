


from Crypto.Cipher import AES
import numpy as np
import cv2
import barcode
from barcode import Code128
from PIL import Image
from barcode.writer import ImageWriter
import cv2
import numpy as np
import imageio
import io
# img = Image.open('1.pgm ').convert('L')
# pixels = ''.join(chr(p) for p in img.getdata() if ord(chr(p)) < 128)
# code128 = Code128(pixels)


img = Image.open("1.pgm")
# Конвертируем изображение в монохромный формат (если необходимо)
img = img.convert('L')

# Получаем данные о пикселях в виде последовательности
pixels = img.getdata()

# Преобразуем пиксели в строку чисел
pixels_str = ''.join(str(p) for p in list(pixels)[:16])



###Рабочий код

ean = barcode.get('code128',pixels_str , writer=ImageWriter())
filename = ean.save('barcode_128')

# ean = barcode.get('code128', '123456789102', writer=ImageWriter())
# filename = ean.save('barcode_ean13')