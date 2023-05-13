
import cv2
from stegano import lsb
from barcode import EAN8,Code128
from barcode.writer import ImageWriter
from PIL import Image
import numpy as np
import dlib
import cv2
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
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    image = cv2.imread(pic)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    faces = detector(gray, 1)
    for face in faces:
        landmarks = predictor(gray, face)
        face_points = [(p.x, p.y) for p in landmarks.parts()][31:68]
    num = int(''.join([str(x[0]) + str(x[1]) for x in face_points]))
    for face in faces:
        landmarks = predictor(gray, face)
        for n in range(31, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
            image.save()
    return num
# print(Exctract('4.jpg'))

def BarCodeimage(pic):
    data = Exctract(pic)
    # result = pic.split(".")[0]
    file_path = pic
    file_name = os.path.basename(file_path)
    # result = file_name.split(".")[0]
    code128 = Code128(data, writer=ImageWriter())
    barcode_img = code128.save(f'barcodes/barcode{file_name}')
    barcodes.append(barcode_img)
    return  barcode_img


# def Coder(codpic,barcode ):
#     result = []
#     # Открытие изображения
#     image = Image.open(codpic)
#
#     file_path = codpic
#     file_name = os.path.basename(file_path)
#     # result = file_name.split(".")[0]
#     # Запись штрих-кода в скрытый слой изображения
#     encrypted_img = lsb.hide(image, barcode)
#
#
#     encrypted_img.save(f'crypt/{file_name}.png')
#     encrypts.append(f"crypt/{file_name}.png")
#     return f"crypt/{file_name}.png"
#
# # print(Coder("pics/9338489.1.jpg","barcodes/barcode9338489.png" ))
#
# def Decoder(img):
#     result = []
#     img = Image.open(img)
#     try:
#         # Извлечение скрытой информации из изображения
#         hidden_data = lsb.reveal(img)
#         result.append(hidden_data)
#         img_Dec = Image.open(str(hidden_data))
#         datas = decode(img_Dec)
#         for i in datas:
#             result.append(i.data.decode("utf-8"))
#             result.append(i.type)
#     except Exception:
#         result.append("Скрытый слой не найден")
#

    return result
class Steganography:
    def coder(self, cover_file, secret_file, color_plane, pixel_bit):
        cover_array = self.image_to_matrix(cover_file)
        secret_array = self.image_to_matrix(secret_file)
        mask = 0xff ^ (1 << pixel_bit)
        secret_bits = ((secret_array[...,color_plane] >> 7) << pixel_bit)
        height, width, _ = secret_array.shape
        cover_plane = (cover_array[:height,:width,color_plane] & mask) + secret_bits
        cover_array[:height,:width,color_plane] = cover_plane
        stego_image = self.matrix_to_image(cover_array)
        return stego_image

    def decoder(self, stego_file, color_plane, pixel_bit):
        stego_array = self.image_to_matrix(stego_file)
        change_index = [0, 1, 2]
        change_index.remove(color_plane)
        stego_array[...,change_index] = 0
        stego_array = ((stego_array >> pixel_bit) & 0x01) << 7
        exposed_secret = self.matrix_to_image(stego_array)
        return exposed_secret

    def image_to_matrix(self, file_path):
        return np.array(Image.open(file_path))

    def matrix_to_image(self, array):
        return Image.fromarray(array)


plane = 2
bit = 1

cover_file = "crypt.jpg"
# secret_file = "barcodes/barcode9338489.12.jpg.png"
secret_file = "codes.png"

stego_file = "stego.png"
extracted_file = "extracted.png"

# S = Steganography()
# S.embed(cover_file, secret_file, plane, bit).save(stego_file)
# S.extract(stego_file, plane, bit).save(extracted_file)
