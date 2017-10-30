# DigitsNeuralNetwork
__[Eng]__ This repo contains neural network which is used to recognize digits on grayscale images with 100x100 size (white backgound and black foreground).
I use competative learning method - "winner takes all"!

__Note:__ Digits represented by 'Avenir' font. Also they should be placed in the center of images.

## Project structure:
* __images/learning__ - contains images for learning;
* __images/test__ - contains images for testing;
* __NeuralNetwork.py__ - contains class which implements neural network;
* __ImageModel.py__ - contains class which holds needed information for network about image 
  such as *pixels converted to signals* and *correct answer*;
* __utils.py__ - contains auxiliary methods connected with *reading images* from file system,
  *parsing correct answer* from the filename, etc.
* __main.py__ - contains client code.

#####################################################################################

__[Укр]__ Цей репозиторій містить реалізацію нейронної мережі, котра вміє розпізнавати цифри на чорнобілих зображеннях розміром 100х100 (чорні цифри на білому фоні).
Я використав метод навчання змаганням - "переможець отримує все"!

__Примітка:__ Для зображення цифр використовується шрифт 'Avenir'. Цифри повинні бути розміщенними в центрі зображення.

## Структура проекту:
* __images/learning__ - містить зображення, які використовується для навчання;
* __images/test__ - містить зображення, які використовуються для перевірки роботи мережі;
* __NeuralNetwork.py__ - містить клас, що реалізує нейронну мережу;
* __ImageModel.py__ - містить клас, який має всю необхідну для нейронної мережі інформацію стосовно зображення, а саме *пікселі перетворені в сигнали* та *правильну відповідь*;
* __utils.py__ - містить допоміжні методі пов'язані з *зчитування зображень* з файлової системи, *парсингом правильної відповіді* з назви файлу, тощо;
* __main.py__ - містить клієнтський код.
