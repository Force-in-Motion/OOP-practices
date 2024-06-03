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
        :return: Возвращает статус True / False
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
            raise TypeError('Получен не верный тип данных, ожидалось булевое значение')
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
        result = [str(i) for i in self.__list_of_purchased_cars]
        return '\n'.join(result)

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

        if data not in self.__list_of_purchased_cars:
            raise ValueError('Данные отсутствуют в списке')

        self.__list_of_purchased_cars.remove(data)

    def __str__(self):
        return (f'Имя покупателя: {self.__name}\n'
                f'Телефон покупателя: {self.__phone}\n'
                f'Почта покупателя: {self.__email}\n'
                f'Список купленных машин:\n{self.get_list_of_purchased_cars()}')

class Salesperson:

    __name: str
    __work_experience: int
    __list_sales_cars: list[Car]

    def __init__(self, name: str, work_experience: int, list_sales_cars: list[Car] = None):
        """
        Формирует шаблон объекта Salesperson
        :param name: Пренимает имя сотрудника
        :param work_experience: Пренимает стаж работы сотрудника
        :param list_sales_cars: Пренимает список проданных машин
        """
        self.__name = name
        self.__work_experience = work_experience
        if list_sales_cars is None:
            self.__list_sales_cars = []
        else:
            self.__list_sales_cars = list_sales_cars

    def get_name(self):
        """
        :return: Возвращает имя сотрудника
        """
        return self.__name

    def get_work_experience(self):
        """
        :return: Возвращает стаж работы сотрудника
        """
        return self.__work_experience

    def get_list_sales_cars(self):
        """
        :return: Возвращает список проданных машин
        """
        result = [str(i) for i in self.__list_sales_cars]
        return '\n'.join(result)

    def set_name(self):
        """
        азначает имя сотрудника
        :return: None
        """
        return self.__name

    def set_work_experience(self):
        """
        Назначает стаж работы сотрудника
        :return: None
        """

    def add_car_in_list_sales_cars(self, data: Car):
        """
        Добавляет машину в список проданных
        :param data: Пренимает машину
        :return: None
        """
        if not isinstance(data, Car):
            raise TypeError('Получен не верный тип данных, ожидались данный типа Car')
        self.__list_sales_cars.append(data)

    def remove_car_in_list_sales_cars(self, data: Car):
        """
        Удаляет машину из списка проданных
        :param data: Пренимает машину
        :return: None
        """
        if not isinstance(data, Car):
            raise TypeError('Получен не верный тип данных, ожидались данный типа Car')

        if data not in self.__list_sales_cars:
            raise ValueError('Данные отсутствуют в списке')

        self.__list_sales_cars.remove(data)

    def sell_car(self, car: Car, customer: Customer, dealer: Dealership, salesperson: Salesperson):
        """
        Продает машину пользователю
        :param car: Пренимает машину
        :param customer: Пренимает покупателя
        :param dealer: Пренимает диллера
        :param salesperson: Пренимает продавца
        :return:
        """
        if not isinstance(car, Car) or not isinstance(customer, Customer) or not isinstance(dealer, Dealership) or not isinstance(salesperson, Salesperson):
            raise TypeError('Получен не верный тип данных, пренимаемые данные могут быть следующих типов: Car, Customer, Dealership, Salesperson')

        if car.get_status() != 'В наличии':
            raise ValueError('Авто нет в наличии')

        else:
            dealer.remove_cars_in_list_of_cars_in_stock(car)
            salesperson.add_car_in_list_sales_cars(car)
            customer.add_car_in_list_of_purchased_cars(car)
            car.set_status('Продано')

    def __str__(self):
        return (f'Имя сотрудника: {self.__name}\n'
                f'Стаж работы сотрудника: {self.__work_experience}\n'
                f'Список проданных машин:\n{self.get_list_sales_cars()}\n')


class Dealership:

    __list_of_cars_in_stock: list[Car]
    __list_of_sellers: list[Salesperson]
    __list_of_all_clients: list[Customer]

    def __init__(self, list_of_cars_in_stock: list[Car] = None, list_of_sellers: list[Salesperson] = None, list_of_all_clients: list[Customer] = None):
        """
        Формирует шаблон объекта Dealership
        :param list_of_cars_in_stock: Пренимает список всех автомобилей в наличии
        :param list_of_sellers: Пренимает список всех сотрудников
        :param list_of_all_clients: Пренимает список всех клиентов
        """
        if list_of_cars_in_stock is None:
            self.__list_of_cars_in_stock = []
        else:
            self.__list_of_cars_in_stock = list_of_cars_in_stock

        if list_of_sellers is None:
            self.__list_of_sellers = []
        else:
            self.__list_of_sellers = list_of_sellers

        if list_of_all_clients is None:
            self.__list_of_all_clients = []
        else:
            self.__list_of_all_clients = list_of_all_clients

    def get_list_of_cars_in_stock(self):
        """
        :return: Возвращает список автомобилей в наличии
        """
        result = [str(i) for i in self.__list_of_cars_in_stock]
        return '\n'.join(result)

    def get_list_of_sellers(self):
        """
        :return: Возвращает список всех сотрудников
        """
        result = [str(i) for i in self.__list_of_sellers]
        return '\n'.join(result)

    def get_list_of_all_clients(self):
        """
        :return: Возвращает список всех клиентов
        """
        result = [str(i) for i in self.__list_of_all_clients]
        return '\n'.join(result)

    def add_cars_in_list_of_cars_in_stock(self, data: Car):
        """
        Добавляет машину в список автомобилей в наличии
        :param data: Пренимает машину
        :return: None
        """
        if not isinstance(data, Car):
            raise TypeError('Получен не верный тип данных, ожидались данный типа Car')
        self.__list_of_cars_in_stock.append(data)

    def add_sellers_in_list_of_sellers(self, data: Salesperson):
        """
        Добавляет сотрудника в список всех сотрудников
        :param data: Пренимает сотрудника
        :return: None
        """
        if not isinstance(data, Salesperson):
            raise TypeError('Получен не верный тип данных, ожидались данный типа Salesperson')
        self.__list_of_sellers.append(data)

    def add_client_in_list_of_all_clients(self, data: Customer):
        """
        Добавляет клиента в список всех клиентов
        :param data: Пренимает клиента
        :return: None
        """
        if not isinstance(data, Customer):
            raise TypeError('Получен не верный тип данных, ожидались данный типа Customer')
        self.__list_of_all_clients.append(data)

    def remove_cars_in_list_of_cars_in_stock(self, data: Car):
        """
        Удаляет машину из списка автомобилей в наличии автомобилей в наличии
        :param data: Пренимает машину
        :return: None
        """
        if not isinstance(data, Car):
            raise TypeError('Получен не верный тип данных, ожидались данный типа Car')

        if data not in self.__list_of_cars_in_stock:
            raise ValueError('Данные отсутствуют в списке')

        self.__list_of_cars_in_stock.remove(data)

    def remove_sellers_in_list_of_sellers(self, data: Salesperson):
        """
        Удаляет сотрудника из списка всех сотрудников
        :param data: Пренимает сотрудника
        :return: None
        """
        if not isinstance(data, Salesperson):
            raise TypeError('Получен не верный тип данных, ожидались данный типа Salesperson')

        if data not in self.__list_of_sellers:
            raise ValueError('Данные отсутствуют в списке')

        self.__list_of_sellers.remove(data)

    def __str__(self):
        return (f'{self.get_list_of_cars_in_stock()}\n'
                f'{self.get_list_of_sellers()}\n'
                f'{self.get_list_of_all_clients()}\n')

class Program:

    @staticmethod
    def main():
        amg = Car('Mersedes', 'amg', 2024, 8247000, 'В наличии')
        m5 = Car('BMW', 'M5', 2023, 914800, 'В наличии')
        volga = Car('Volga', '3110', 1999, 270000, 'В наличии')
        uaz = Car('Uaz', 'Patriot', 2023, 2800000, 'В наличии')

        cl1 = Customer('John', 8924029429824308, 'john@mail.ru')
        cl2 = Customer('Rick', 8924029429824308, 'rick@mail.ru')
        cl3 = Customer('Brad', 8924029429824308, 'brad@mail.ru')

        sel1 = Salesperson('Valera', 5)
        sel2 = Salesperson('Anatoliy', 7)

        dealer = Dealership()

        dealer.add_cars_in_list_of_cars_in_stock(amg)
        dealer.add_cars_in_list_of_cars_in_stock(m5)
        dealer.add_cars_in_list_of_cars_in_stock(volga)
        dealer.add_cars_in_list_of_cars_in_stock(uaz)

        dealer.add_sellers_in_list_of_sellers(sel1)
        dealer.add_sellers_in_list_of_sellers(sel2)

        dealer.add_client_in_list_of_all_clients(cl1)
        dealer.add_client_in_list_of_all_clients(cl2)
        dealer.add_client_in_list_of_all_clients(cl3)

        sel1.sell_car(m5, cl1, dealer, sel1)
        sel2.sell_car(uaz, cl2, dealer, sel2)
        sel2.sell_car(amg, cl3, dealer, sel2)
        print(dealer)
        print(m5)

Program.main()





