from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def speak(self) -> None:
        pass


class Cat(Animal):
    def speak(self) -> None:
        return print('Meeooow!')


class Dog(Animal):
    def speak(self) -> None:
        return print('Au au auuu!')


class Snake(Animal):
    def speak(self) -> None:
        return print('Sssssssss!')


class Bird(Animal):
    def speak(self) -> None:
        return print('!#!@%$#!#!@!~~')


class SimpleFactory:
    def create_animal_speaker(self, type) -> None:
        return eval(type)().speak()


if __name__ == '__main__':
    animal_type = input(
        'Que animal você quer ver falando?\n[Cat, Dog, Snake, Bird]\nEscolha: ')

    factory = SimpleFactory()
    factory.create_animal_speaker(animal_type)
