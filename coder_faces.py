
import cv2
import numpy as np
import imageio

from stegano import lsb
from barcode import EAN8,Code128
from barcode.writer import ImageWriter
from PIL import Image
from pyzbar.pyzbar import decode
import os
Pictures = []
barcodes = []
encrypts = []
def get_pics():

    path = 'Pics'
    files = os.listdir(path)
    for file in files:

        filepath = os.path.join(path, file)
        Pictures.append(filepath)
    return  Pictures


def get_barcodes():

    path = 'barcodes'
    files = os.listdir(path)
    for file in files:

        filepath = os.path.join(path, file)
        barcodes.append(filepath)
    return  barcodes

def get_encrypted_pics():

    path = 'crypt'
    files = os.listdir(path)
    for file in files:

        filepath = os.path.join(path, file)
        encrypts.append(filepath)
    return  encrypts
# print(get_encrypted_pics())
def Exctract(pic):
    face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
    img_rgb = cv2.imread(pic)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    arr = faces
    num_str = ''.join([str(i) for i in arr[0]])
    num = num_str
    return num
# print(Exctract('4.jpg'))

def BarCodeimage(pic):
    data = Exctract(pic)
    # result = pic.split(".")[0]
    file_path = pic
    file_name = os.path.basename(file_path)
    result = file_name.split(".")[0]
    code128 = Code128(data, writer=ImageWriter())
    barcode_img = code128.save(f'barcodes/barcode{result}')
    barcodes.append(barcode_img)
    return  barcode_img


def Coder(codpic,barcode ):
    result = []
    # Открытие изображения
    image = Image.open(codpic)

    file_path = codpic
    file_name = os.path.basename(file_path)
    result = file_name.split(".")[0]
    # Запись штрих-кода в скрытый слой изображения
    encrypted_img = lsb.hide(image, barcode)


    encrypted_img.save(f'crypt/{result}.png')
    encrypts.append(f"crypt/{result}.png")
    return f"crypt/{result}.png"

# print(Coder("pics/9338489.1.jpg","barcodes/barcode9338489.png" ))

def Decoder(img):
    result = []
    img = Image.open(img)
    try:
        # Извлечение скрытой информации из изображения
        hidden_data = lsb.reveal(img)
        result.append(hidden_data)
        img_Dec = Image.open(str(hidden_data))
        datas = decode(img_Dec)
        for i in datas:
            result.append(i.data.decode("utf-8"))
            result.append(i.type)
    except Exception:
        result = "Скрытый слой не найден"


    return result

def Haart_casc():
    face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
    img_rgb = cv2.imread('5.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    data = str(faces)
    ean8 = Code128(data, writer=ImageWriter())
    barcode_img = ean8.save('barcode128')
    decoded_data = decode(Image.open('barcodes/barcode128.png'))
    for i in decoded_data:
        dec = i.data.decode("utf-8")

    if str(faces) == dec:
        print('Face verified!')
    else:
        print('Face not verified!')
# Haart_casc()