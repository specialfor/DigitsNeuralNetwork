import utils

from NeuralNetwork import NeuralNetwork

# Functions
# ---------
# Функції


# Returns images for learning
# ---------------------------
# Повертає вибірку зображень для навчання
def get_learning_images():
    return utils.get_images(learning_directory)


# Returns images for testing
# --------------------------
# Повертає вибірку зображень для перевірки роботи мережі
def get_test_images():
    return utils.get_images(test_directory)


# Checks results of 'network' work on 'images' set
# ------------------------------------------------
# Перевіряє результат роботи мережі на вибірці 'images'
def check_network(network, images):
    for image in images:
        print('Image is taken from file: ' + image.filename)
        print('Is number ' + str(image.answer) + ' ? ' + str(image.answer == network.evaluate(image.pixels)))


# Learns 'network' with 'image_models' set 'epoch_count' times
# ------------------------------------------------------------
# Навчає мережу на виборці 'image_models' 'epoch_count' разів
def study(network, image_models, epoch_count):
    for i in range(epoch_count):
        for model in image_models:
            # Learns network
            # --------------
            # Навчаємо мережу
            network.study(model.pixels, model.answer)


# Constants
learning_directory = "images/learning"
test_directory = "images/test"

# Image has size 100 x 100, so the number of signals is 100^2
# -----------------------------------------------------------
# Розмір зображеннь 100 х 100, тому нейронна мережа приймає 100^2 сигналів
number_of_inputs = 100 * 100
number_of_outputs = 10 # ten digits / 10 цифр
epoch_count = 100

# Main
learning_images = get_learning_images()

# Creates network and studies it
# ------------------------------
# Створюємо об'єкт 'NeuralNetwork' і навчаємо його
network = NeuralNetwork(number_of_inputs, number_of_outputs)
study(network, learning_images, epoch_count)

# Checks on images for learning
# -----------------------------
# Перевіряємо роботу мережі на навчальній виборці
print('##### LEARNING IMAGES #####')
check_network(network, learning_images)
print('###########################')

print()
print()

# Checks on images for testing
# ----------------------------
# Перевіряємо роботу мережі на тестовій виборці
testing_images = get_test_images()
print('##### TESTING IMAGES #####')
check_network(network, testing_images)
