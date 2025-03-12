from __future__ import annotations

class Animal:

    _name: str
    _species: str

    def __init__(self, name: str, species: str):
        """
        Формирует шаблон объекта Animal
        :param name: Пренимает имя животного
        :param species: Пренимает разновидность животного
        """
        self._name = name
        self._species = species

    def make_sound(self) -> str:
        """
        Переопределяет звук, издаваемый животным
        :return: None
        """
        return f'Rrrrrrr'

    def __str__(self) -> str:
        """
        :return: Возвращает строковое представление объекта
        """
        return (f'Имя: {self._name}\n'
                f'Разновидность: {self._species}\n')

class Cat(Animal):

    _name: str
    _species: str
    __age: int

    def __init__(self, name: str, species: str, age: int):
        """
        Формирует шаблон объекта Cat
        :param name: Пренимает имя
        :param species: Пренимает разновидность
        :param age: Роенимает возраст
        """
        super().__init__(name, species)
        self.__age = age

    def make_sound(self) -> str:
        """
        Переопределяет звук, издаваемый животным
        :return: None
        """
        return 'Meeoooooowwww'

    def __str__(self) -> str:
        """
        :return: Возвращает строковое представление объекта
        """
        return (f'Имя: {self._name}\n'
                f'Разновидность: {self._species}\n'
                f'Возраст: {self.__age}\n')

class Dog(Animal):

    _name: str
    _species: str
    __color: str

    def __init__(self, name: str, species: str, color: str):
        """
        Формирует шаблон объекта Dog
        :param name: ренимает имя
        :param species: Пренимает разновидность
        :param color: Пренимает цвет
        """
        super().__init__(name, species)
        self.__color = color

    def make_sound(self) -> str:
        """
        Переопределяет звук, издаваемый животным
        :return: None
        """
        return 'Wooooooffff'

    def __str__(self) -> str:
        """
        :return: Возвращает строковое представление объекта
        """
        return (f'Имя: {self._name}\n'
                f'Разновидность: {self._species}\n'
                f'Цвет: {self.__color}\n')


class Bird(Animal):

    _name: str
    _species: str
    __fly: bool

    def __init__(self, name: str, species: str, fly: bool):
        """
        Формирует шаблон объекта Bird
        :param name: Пренимает имя
        :param species: Пренимает разновидность
        :param fly: летает или нет
        """
        super().__init__(name, species)
        self.__fly = fly

    def __str__(self) -> str:
        """
        :return: Возвращает строковое представление объекта
        """
        return (f'Имя: {self._name}\n'
                f'Разновидность: {self._species}\n'
                f'Полет: {self.__fly}\n')

    def make_sound(self) -> str:
        """
        Переопределяет звук, издаваемый животным
        :return: None
        """
        return 'Grrraaaaaagggg'


class Program:

    @staticmethod
    def main():
        cat = Cat('Puh', 'cat', 12)
        dog = Dog('Jeck', 'dog', 'Red')
        bird = Bird('Chir', 'Bird', True)

        print(cat)
        print(dog)
        print(bird)
        print(cat.make_sound())
        print(dog.make_sound())
        print(bird.make_sound())

Program.main()
