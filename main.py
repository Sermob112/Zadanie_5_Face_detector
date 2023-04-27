


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
from stegano import lsb
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
from pyzbar.pyzbar import decode

def Hide_image():
    #Создание штрих-кода
    data = '123456789'
    code128 = Code128(data, writer=ImageWriter())
    barcode_img = code128.save('barcode')

    # Открытие изображения
    image = Image.open('4.jpg')

    # Запись штрих-кода в скрытый слой изображения
    encrypted_img = lsb.hide(image, 'barcode.png')

    # Сохранение скрытого изображения
    encrypted_img.save('encrypted_image.png')

def decoder():
    img = Image.open("encrypted_image.png")

    # Извлечение скрытой информации из изображения
    hidden_data = lsb.reveal(img)
    img_Dec = Image.open(str(hidden_data))
    result = decode(img_Dec)
    for i in result:
        print(i.data.decode("utf-8"))

decoder()
