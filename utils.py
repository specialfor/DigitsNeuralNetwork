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

# Enumerates files in directory with name 'directory_name'. Returns list of files names.
# -------------------------------------------------------------------------------------
# Перебирає файли в директорії з ім'ям 'directory_name'. Повертає список імен файлів.
def enumerate_files(directory_name):
    file_names = []

    for (dirpath, dirnames, filenames) in walk(directory_name):
        file_names.extend(filenames)

    return file_names


# Get answer from file with name 'file_name'.
# Note: file should begin with word from keys of 'answers' dictionary.
# --------------------------------------------------------------------
# Парсить цифру, що зображена на картинці з імені файлу.
# Щоб парсинг пройшов вдало, треба, щоб назва файлу починилася
# будь-яким ключем словника 'answers'
def get_answer(file_name):
    name = file_name.rsplit('.png', 1)[0]
    key = name.split('_', 1)[0]
    return answers[key]


# Get bitmap from image, normalize color values and transform it to
# a list of signals: 1 - black color, 0 - white color.
# -----------------------------------------------------------------------
# Стягує з картинки матрицю пікселей, нормалізує значення кольору
# і транфсормує їх в сигнали: 1 - чорний колір, 0 - білий колір
def convert_to_bitmap(image):
    pixels = []

    # Every pixel has 3 component (rgb).
    # Because of our images have white background
    # and black foreground, we can take only the 1st component
    # (others are the same as the 1st).
    # --------------------------------------------------------
    # Кожен піксель має 3 компонети (червоний, зелений і синій).
    # Завдяки тому, що наші зображень мають білий фон, а цифрі
    # зафарбовані в чорний, ми можемо взяти лише 1 компонент
    # (інші будуть такі самі як і 1 компонент).
    for rgb in list(image.getdata()):
        pixels.append(abs(rgb[0] / 255 - 1))

    return pixels


# Returns list of 'ImageModel' instances
# which is used to learn network or check network.
# ------------------------------------------------
# Повертає список об'єктів 'ImageModel', що
# використовується для навчання або перевірки мережі.
def get_images(directory_name):
    images = []

    for file_name in enumerate_files(directory_name):
        # Takes only files which end with '.png'
        # -------------------------------------
        # Беремо тільки ті файли, котрі мають закінчення '.png'
        if file_name.rfind('.png') != -1:
            image = Image.open(directory_name + '/' + file_name)
            pixels = convert_to_bitmap(image)
            answer = get_answer(file_name)
            images.append(ImageModel(file_name, pixels, answer))

    return images
