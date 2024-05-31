from __future__ import annotations

class Student:

    __name: str
    __surname: str
    __age: int
    __average_score: int

    def __init__(self, name: str, surname: str, age: int, average_score: int):
        """
        Формирует шаблон класса Student
        :param name: Пренимает имя
        :param family: Пренимает фамилию
        :param age: Пренимает возраст
        :param average_score: Пренимает средний балл
        """
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__average_score = average_score

    def get_name(self):
        """
        :return: Возвращает имя студента
        """
        return self.__name

    def get_surname(self):
        """
        :return: Возвращает фамилию студента
        """
        return self.__surname

    def get_age(self):
        """
        :return: Возвращает возраст студента
        """
        return self.__age

    def get_average_score(self):
        """
        :return: Возвращает средний балл студента
        """
        return self.__average_score

    def set_name(self, data: str):
        """
        Назначает имя студента
        :param data:
        :return: None
        """
        self.__name = data

    def set_surname(self, data: str):
        """
        Устанавливает фамилию студента
        :param data:
        :return: None
        """
        self.__surname = data

    def set_age(self, data: int):
        """
        Назначает возраст
        :param data:
        :return: None
        """
        self.__age = data

    def set_average_score(self, data: int):
        """
        Назначает средний балл
        :param data:
        :return: None
        """
        self.__average_score = data

    def __eq__(self, other: int):
        """
        Определяет поведение оператора равенства ==
        :param other: Пренимает правый операнд для сравнения
        :return:
        """
        if not isinstance(self or other, int):
            raise TypeError('Передан не верный тип данных, ожидается целое число')
        return True if self.__average_score == other else False

    def __ne__(self, other: int):
        """
        Определяет поведение оператора неравенства !=
        :param other: Пренимает правый операнд для сравнения
        :return:
        """
        if not isinstance(self or other, int):
            raise TypeError('Передан не верный тип данных, ожидается целое число')
        return self.__average_score != other

    def __lt__(self, other: int):
        """
        Определяет поведение оператора меньше <
        :param other: Пренимает правый операнд для сравнения
        :return:
        """
        if not isinstance(self or other, int):
            raise TypeError('Передан не верный тип данных, ожидается целое число')
        return self.__average_score < other

    def __gt__(self, other: int):
        """
        Определяет поведение оператора больше >
        :param other: Пренимает правый операнд для сравнения
        :return:
        """
        if not isinstance(self or other, int):
            raise TypeError('Передан не верный тип данных, ожидается целое число')
        return self.__average_score > other

    def __le__(self, other: int):
        """
        Определяет поведение оператора меньше или равно <=
        :param other: Пренимает правый операнд для сравнения
        :return:
        """
        if not isinstance(self or other, int):
            raise TypeError('Передан не верный тип данных, ожидается целое число')
        return self.__average_score <= other

    def __ge__(self, other: int):
        """
        Определяет поведение оператора больше или равно >=
        :param other: Пренимает правый операнд для сравнения
        :return:
        """
        if not isinstance(self or other, int):
            raise TypeError('Передан не верный тип данных, ожидается целое число')
        return self.__average_score >= other

    def __str__(self):
        return (f'Имя студента: {self.__name}\n'
                f'Фамилия студента: {self.__surname}\n'
                f'Возраст студента: {self.__age}\n'
                f'Средний балл студента: {self.__average_score}\n')


class Program:

    @staticmethod
    def main():
        st1 = Student('Колян', 'Филатов', 28, 78)
        st2 = Student('Кеша', 'Геворгян', 21, 89)

        print(st1)
        print(st2)

        st1.set_average_score(89)

        print(st1.get_average_score() == st2.get_average_score())

        st2.set_average_score(28)

        print(st1.get_average_score() > st2.get_average_score())

Program.main()