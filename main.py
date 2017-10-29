import utils

from NeuralNetwork import NeuralNetwork

# Functions
def get_learning_images():
    return utils.get_images(learning_directory)


def get_test_images():
    return utils.get_images(test_directory)


def check_network(network, images):
    for image in images:
        print('Image is taken from file: ' + image.filename)
        print('Is number ' + str(image.answer) + ' ? ' + str(image.answer == network.evaluate(image.pixels)))


def study(network, image_models, epoch_count):
    for i in range(epoch_count):
        for model in image_models:
            network.study(model.pixels, model.answer)


# Constants
learning_directory = "learning"
test_directory = "test"

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
print()
print()

# Check on test images
testing_images = get_test_images()
print('##### TESTING IMAGES #####')
check_network(network, testing_images)