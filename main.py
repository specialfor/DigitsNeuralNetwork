from PIL import Image
from os import walk

from neural import NeuralNetwork
from ImageModel import ImageModel

learning_directory = "learning"
test_directory = "test"

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

# functions
def enumarate_files_in(directory_name):
    file_names = []

    for (dirpath, dirnames, filenames) in walk(directory_name):
        file_names.extend(filenames)

    return file_names


def get_answer(file_name):
    name = file_name.split('.', 1)[0]
    key = name.split('_', 1)[0]
    return answers[key]


def convert_to_bitmap(image):
    pixels = []

    for rgb in list(image.getdata()):
        pixels.append(abs(rgb[0] / 255 - 1))

    return pixels


def get_images(directory_name):
    images = []

    for file_name in enumarate_files_in(directory_name):
        image = Image.open(directory_name + '/' + file_name)
        pixels = convert_to_bitmap(image)
        answer = get_answer(file_name)
        images.append(ImageModel(file_name, pixels, answer))

    return images


def get_learning_images():
    return get_images(learning_directory)


def get_test_images():
    return get_images(test_directory)


def check_network(network, images):
    for image in images:
        print('Image is taken from file: ' + image.filename)
        print('Is number ' + str(image.answer) + ' ? ' + str(image.answer == network.evaluate(image.pixels)))


def study(network, image_models, epoch_count):
    for i in range(epoch_count):
        for model in image_models:
            network.study(model.pixels, model.answer)


# Constants
number_of_inputs = 100 * 100
number_of_outputs = 10
epoch_count = 100

# Main
learning_images = get_learning_images()

# Create network and study it
network = NeuralNetwork(number_of_inputs, number_of_outputs)
study(network, learning_images, epoch_count)

# Check on learning images
print('##### LEARNING IMAGES #####')
check_network(network, learning_images)
print('###########################')

# Check on test images
testing_images = get_test_images()
print('##### TESTING IMAGES #####')
check_network(network, testing_images)