from PIL import Image
from stegano import lsb
# def get_lsb(image_path):
#     # Открываем изображение
#     image = Image.open(image_path)
#
#     # Создаем пустое изображение того же размера
#     lsb_image = Image.new("RGB", image.size)
#
#     # Получаем пиксели изображения
#     pixels = image.load()
#     lsb_pixels = lsb_image.load()
#
#     # Извлекаем младшие биты каждого пикселя и устанавливаем их в lsb_image
#     for i in range(image.width):
#         for j in range(image.height):
#             r, g, b = pixels[i, j]
#             # Получаем младшие биты каждого канала
#             r_lsb = r & 1
#             g_lsb = g & 1
#             b_lsb = b & 1
#             # Устанавливаем младшие биты в lsb_image
#             lsb_pixels[i, j] = (r_lsb * 255, g_lsb * 255, b_lsb * 255)
#
#     # Показываем изображение с младшими битами
#     lsb_image.show()
#
# # Пример использования
# image_path = "EXIT.jpg"
# get_lsb(image_path)
#
# def resize_images(image1_path, image2_path):
#     # Открываем изображения
#     image1 = Image.open(image1_path)
#     image2 = Image.open(image2_path)
#
#     # Получаем размеры изображений
#     width1, height1 = image1.size
#     width2, height2 = image2.size
#
#     # Проверяем размеры изображений
#     if width1 != width2 or height1 != height2:
#         # Меняем размер второго изображения
#         resized_image2 = image2.resize((width1, height1))
#         return image1, resized_image2
#     else:
#         return image1, image2
#
# # Пример использования
#
# def merge_images(image_path, secret_image_path, output_path):
#     # Открываем изображения
#     image = Image.open(image_path)
#     secret_image = Image.open(secret_image_path)
#
#     image, secret_image = resize_images(image_path, secret_image_path)
#     if image.size != secret_image.size:
#         print("Ошибка: размеры изображений не совпадают.")
#         return
#
#     # Создаем пустое изображение для записи младших битов
#     merged_image = Image.new("RGB", image.size)
#
#     # Получаем пиксели изображений
#     pixels = image.load()
#     secret_pixels = secret_image.load()
#     merged_pixels = merged_image.load()
#
#     # Записываем младшие биты пикселей secret_image в merged_image
#     for i in range(image.width):
#         for j in range(image.height):
#             r, g, b = pixels[i, j]
#             sr, sg, sb = secret_pixels[i, j]
#             # Записываем младшие биты из secret_image в пиксель merged_image
#             merged_pixels[i, j] = ((r & 0xFE) | (sr & 1), (g & 0xFE) | (sg & 1), (b & 0xFE) | (sb & 1))
#
#     # Сохраняем объединенное изображение
#     merged_image.save(output_path)
#
# # Пример использования
# image_path = "crypt.jpg"
# secret_image_path = "5.jpg"
# output_path = "EXIT.jpg"

#
# merge_images(image_path, secret_image_path, output_path)


import numpy as np
from PIL import Image

class Steganography:
    def embed(self, cover_file, secret_file, color_plane, pixel_bit):
        cover_array = self.image_to_matrix(cover_file)
        secret_array = self.image_to_matrix(secret_file)
        mask = 0xff ^ (1 << pixel_bit)
        secret_bits = ((secret_array[...,color_plane] >> 7) << pixel_bit)
        height, width, _ = secret_array.shape
        cover_plane = (cover_array[:height,:width,color_plane] & mask) + secret_bits
        cover_array[:height,:width,color_plane] = cover_plane
        stego_image = self.matrix_to_image(cover_array)
        return stego_image

    def extract(self, stego_file, color_plane, pixel_bit):
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

S = Steganography()
S.embed(cover_file, secret_file, plane, bit).save(stego_file)
S.extract(stego_file, plane, bit).save(extracted_file)
