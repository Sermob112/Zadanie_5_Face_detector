
from stegano import lsb
import cv2
import numpy as np
import imageio

from stegano import lsb
from barcode import EAN8,Code128
from barcode.writer import ImageWriter
from PIL import Image
from pyzbar.pyzbar import decode


# Загружаем детектор лица
import dlib
import cv2
def points_to_bbarcode(image):
# Загружаем предобученную модель
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    faces = detector(gray, 1)
    for face in faces:
        landmarks = predictor(gray, face)
        face_points = [(p.x, p.y) for p in landmarks.parts()][31:68]
    num = int(''.join([str(x[0]) + str(x[1]) for x in face_points]))

    print(num)
    for face in faces:
        landmarks = predictor(gray, face)
        for n in range(31, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow("Face Landmarks", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# # Сохраняем изображение с отмеченными точками
# cv2.imwrite("face_landmarks.jpg", image)


# img = Image.open('9338489.png')
#
# # Извлекаем биты изображения
# lsb = ''.join([bin(x)[-1] for x in img.tobytes()])
#
# img = cv2.imread('9338489.png')
# red_channel = img[:, :, 2]
# lsb_mask = 0b00000010
# red_lsb = red_channel & lsb_mask
# cv2.imshow('Red LSB', red_lsb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def Exctract(pic):
    face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
    img_rgb = cv2.imread(pic)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    arr = faces
    num_str = ''.join([str(i) for i in arr[0]])
    num = num_str
    return num
# print(Exctract('5.jpg'))
def BarCodeimage(pic):
    data = Exctract(pic)
    result = pic.split(".")[0]
    code128 = Code128(data, writer=ImageWriter())
    barcode_img = code128.save(f'barcodes/barcode{result}')
    return  barcode_img
# print(BarCodeimage('5.jpg'))
def Coder(codpic,barcode ):
    # Открытие изображения
    image = Image.open(codpic)

    # Запись штрих-кода в скрытый слой изображения
    encrypted_img = lsb.hide(image, barcode)

    # Сохранение скрытого изображения
    encrypted_img.save('encrypted_image.png')
# print(Coder("5.jpg","barcodes/barcode5.png" ))

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

# print(Decoder("encrypted_image.png"))