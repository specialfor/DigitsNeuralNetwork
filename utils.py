from PIL import Image
from os import walk

from ImageModel import ImageModel

answers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def enumarate_files(directory_name):
    file_names = []

    for (dirpath, dirnames, filenames) in walk(directory_name):
        file_names.extend(filenames)

    return file_names


def get_answer(file_name):
    name = file_name.rsplit('.png', 1)[0]
    key = name.split('_', 1)[0]
    return answers[key]


def convert_to_bitmap(image):
    pixels = []

    for rgb in list(image.getdata()):
        pixels.append(abs(rgb[0] / 255 - 1))

    return pixels


def get_images(directory_name):
    images = []

    for file_name in enumarate_files(directory_name):
        if file_name.rfind('.png') != -1:
            image = Image.open(directory_name + '/' + file_name)
            pixels = convert_to_bitmap(image)
            answer = get_answer(file_name)
            images.append(ImageModel(file_name, pixels, answer))

    return images