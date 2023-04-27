
import cv2
import numpy as np
import imageio

from stegano import lsb
from barcode import EAN8,Code128
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

def decoder(img):
    img = Image.open("encrypted_image.png")

    # Извлечение скрытой информации из изображения
    hidden_data = lsb.reveal(img)
    img_Dec = Image.open(str(hidden_data))
    result = decode(img_Dec)
    for i in result:
        print(i.data.decode("utf-8"))

# decoder()
def Haart_casc():
    face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
    img_rgb = cv2.imread('5.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    data = str(faces)
    ean8 = Code128(data, writer=ImageWriter())
    barcode_img = ean8.save('barcode128')
    decoded_data = decode(Image.open('barcode128.png'))
    for i in decoded_data:
        dec = i.data.decode("utf-8")

    if str(faces) == dec:
        print('Face verified!')
    else:
        print('Face not verified!')
Haart_casc()