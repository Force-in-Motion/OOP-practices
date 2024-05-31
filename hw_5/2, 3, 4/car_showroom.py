from __future__ import annotations

class Car:

    __brand: str
    __model: str
    __year_of_issue: int
    __price: float
    __status: str

    def __init__(self,  brand: str, model: str, year_of_issue: int, price: float, status: str):
        """
        Формирует шаблон объекта Car
        :param brand: Пренимает бренд машины
        :param model: Пренимает модель машины
        :param year_of_issue: Пренимает год производства
        :param price: Пренимает цену
        :param status: Пренимает статус (в наличии, продано, ожидается)
        """
        self.__brand = brand
        self.__model = model
        self.__year_of_issue = year_of_issue
        self.__price = price
        self.__status = status

    def get_brand(self):
        """
        :return: Возвращает название бренда
        """
        return self.__brand

    def get_model(self):
        """
        :return: Возвращает название модели
        """
        return self.__model

    def get_year_of_issue(self):
        """
        :return: Возвращает год производства
        """
        return self.__year_of_issue

    def get_price(self):
        """
        :return: Возвращает цену
        """
        return self.__price

    def get_status(self):
        """
        :return: Возвращает статус (в наличии, продано, ожидается)
        """
        return self.__status

    def set_brand(self, data: str):
        """
        Назначает бренд
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__brand = data

    def set_model(self, data: str):
        """
        Назначает модель
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__model = data

    def set_year_of_issue(self, data: int):
        """
        Назначает год производства
        :return: None
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')
        self.__year_of_issue = data

    def set_price(self, data: float):
        """
        Назначает цену
        :return: None
        """
        if not isinstance(data, float):
            raise TypeError('Получен не верный тип данных, ожидалось число')
        self.__price = data

    def set_status(self, data: str):
        """
        Назначает статус
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__status = data

    def __str__(self):
        """
        :return: Возвращает строковое представление объекта
        """
        return (f'Название бренда: {self.__brand}\n'
                f'Название модели: {self.__model}\n'
                f'Год производства: {self.__year_of_issue}\n'
                f'Цена: {self.__price}\n'
                f'Статус: {self.__status}\n')


class Customer:

    __name: str
    __phone: int
    __email: str
    __list_of_purchased_cars: list[Car]

    def __init__(self, name: str, phone: int, email: str, list_of_purchased_cars: list[Car] = None):
        """
        Формирует шаблон объекта Customer
        :param name: Пренимает имя покупателя
        :param phone: Пренимает телефон покупателя
        :param email: Пренимает email покупателя
        :param list_of_purchased_cars: Пренимает список, купленных покупателем, машин
        """
        self.__name = name
        self.__phone = phone
        self.__email = email
        if list_of_purchased_cars is None:
            self.__list_of_purchased_cars = []
        else:
            self.__list_of_purchased_cars = list_of_purchased_cars

    def get_name(self):
        """
        :return: Возвращает имя покупателя
        """
        return self.__name

    def get_phone(self):
        """
        :return: Возвращает телефон покупателя
        """
        return self.__phone

    def get_email(self):
        """
        :return: Возвращает email покупателя
        """
        return self.__email

    def get_list_of_purchased_cars(self):
        """
        :return: Возвращает список, купленных покупателем, машин
        """
        return self.__list_of_purchased_cars

    def set_name(self, data: str):
        """
        Назначает имя покупателя
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__name = data

    def set_phone(self, data: int):
        """
        Назначает телефон покупателя
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалсь целое число')
        self.__name = data

    def set_email(self, data: str):
        """
        Назначает почту покупателя
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__name = data

    def add_car_in_list_of_purchased_cars(self, data: Car):
        """
        Добавляет машину в список купленных
        :param data: Пренимает машину
        :return: None
        """
        if not isinstance(data, Car):
            raise TypeError('Получен не верный тип данных, ожидались данный типа Car')
        self.__list_of_purchased_cars.append(data)

    def remove_car_in_list_of_purchased_cars(self, data: Car):
        """
        Удаляет машину из списка купленных
        :param data: Пренимает машину
        :return: None
        """
        if not isinstance(data, Car):
            raise TypeError('Получен не верный тип данных, ожидались данный типа Car')
        self.__list_of_purchased_cars.remove(data)

    def __str__(self):
        return (f'Имя покупателя: {self.__name}\n'
                f'Телефон покупателя: {self.__phone}\n'
                f'Почта покупателя: {self.__email}\n'
                f'Список купленных машин: {self.__list_of_purchased_cars}\n')

class Salesperson:
    pass






class Dealership:
    pass




class Program:
    pass





