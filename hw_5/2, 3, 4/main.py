from __future__ import annotations

class Book:

    title: str
    author: str
    year_publishing: int
    id_book: int
    list_genre: list[Genre]

    def __init__(self, title: str, author: str, year_publishing: int, id_book: int, list_genre: list[Genre] = None):
        """
        Формирует шаблон класса library
        :param title: Пренимает название
        :param author: Пренимает автора
        :param year_publishing: Пренимает год издания
        :param id_book: Пренимает ID книги
        :param list_genre: Пренимает список объектов класса Genre
        """
        self.__title = title
        self.__author = author
        self.__year_publishing = year_publishing
        self.__id_book = id_book
        if list_genre is None:
            self.__list_genre = []
        self.__list_genre = list_genre

    def get_title(self):
        """
        :return: Возвращает название
        """
        return self.__title

    def get_author(self):
        """
        :return: Возвращает автора
        """
        return self.__author

    def get_year_publishing(self):
        """
        :return: Возвращает год издания
        """
        return self.__year_publishing

    def get_id_book(self):
        """
        :return: Возвращает ID книги
        """
        return self.__id_book

    def get_list_genre(self):
        """
        :return: озвращает список жанров объекта  Genre
        """
        return self.__list_genre

    def set_title(self, data: str):
        """
        :return: Возвращает название
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__title = data

    def set_author(self, data: str):
        """
        :return: Возвращает автора
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__author = data

    def set_year_publishing(self, data: int):
        """
        :return: Возвращает год издания
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')
        self.__year_publishing = data

    def set_id_book(self, data: int):
        """
        :return: Возвращает ID книги
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')
        self.__id_book = data

    def add_genre(self, data: Genre):
        """
        Добавляет жанр в список жанров книги
        :param data: Пренимает новый жанр
        :return: None
        """
        if not isinstance(data, Genre):
            raise TypeError('Получен не верный тип данных, ожидались данные типа Genre')
        self.__list_genre.append(data)

    def remove_genre(self, data: Genre):
        """
        Удаляет жанр из списка жанров книги
        :param data: Пренимает жанр, который требуется удалить
        :return: None
        """
        if not isinstance(data, Genre):
            raise TypeError('Получен не верный тип данных, ожидались данные типа Genre')
        self.__list_genre.remove(data)

    def __str__(self):
        """
        :return: Возвращает строковое представление объекта
        """
        return (f'Название книги: {self.__title}\n'
                f'Автор книги: {self.__author}'
                f'Год публикации книги: {self.__year_publishing}\n'
                f'ID книги: {self.__id_book}\n'
                f'Список жанров книги: {self.__list_genre}\n')


class Genre:

    name: str
    description: str

    def __init__(self, name: str, description: str):
        """
        Формирует шаблон объекта Genre
        :param name: Пренимает название жанра
        :param description: Пренимает описание жанра
        """
        self.__name = name
        self.__description = description

    def get_name(self):
        """
        :return: Возвращает название жанра
        """
        return self.__name

    def get_description(self):
        """
        :return: Возвращает описание жанра
        """
        return self.__description

    def set_name(self, data: str):
        """
        Назначает название жанра
        :param data: Пренимает название жанра
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__name = data

    def set_description(self, data: str):
        """
        Назначает описание жанра
        :param data: Пренимает описание жанра
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__description = data

    def __str__(self):
        """
        :return: Возвращает строковое представление объекта Genre
        """
        return (f'Название жанра: {self.__name}\n'
                f'Описание жанра: {self.__description}\n')


class ContactInfo:

    type_contact: str
    value_contact: str or int

    def __init__(self, type_contact: str, value_contact: str or int):
        """
        Формирует шаблон объекта ContactInfo
        :param type_contact: Пренимает тип контакта
        :param value_contact: значение контакта
        """
        self.__type_contact = type_contact
        self.__value_contact = value_contact

    def get_type_contact(self):
        """
        :return: Возвращает тип контакта
        """
        return self.__type_contact

    def get_value_contact(self):
        """
        :return: Возвращает значение контакта
        """
        return self.__value_contact

    def set_type_contact(self, data: str):
        """
        Назначает тип контакта
        :param data: Пренимает тип контакта
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__type_contact = data

    def set_value_contact(self, data: str):
        """
        Назначает тип контакта
        :param data: Пренимает тип контакта
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__value_contact = data

    def __str__(self):
        """
        :return: Возвращает строковое представление объекта ContactInfo
        """
        return (f'Тип контакта: {self.__type_contact}\n'
                f'Значение контакта: {self.__value_contact}\n')

class Employee:

    name: str
    job_position: str
    id_employee: int
    contact_info: list[ContactInfo]

    def __init__(self, name: str, job_position: str, id_employee: int, contact_info: list[ContactInfo] = None):
        """
        Формирует шаблон объекта Employee
        :param name: Пренимает имя сотрудника
        :param job_position: Пренимает занимаемую должность сотрудника
        :param id_employee: Пренимает ID сотрудника
        :param contact_info: Пренимает список объектов класса ContactInfo
        """
        self.__name = name
        self.__job_position = job_position
        self.__id_employee = id_employee
        if contact_info is None:
            self.__contact_info = []
        self.__contact_info = contact_info

    def get_name(self):
        """
        :return: Возвращает имя сотрудника
        """
        return self.__name

    def get_job_position(self):
        """
        :return: Возвращает занимаемую должность сотрудника
        """
        return self.__job_position

    def get_id_employee(self):
        """
        :return: Возвращает ID сотрудника
        """
        return self.__id_employee

    def get_contact_info(self):
        """
        :return: Возвращает список объектов класса ContactInfo
        """
        return self.__contact_info

    def set_name(self, data: str):
        """
        Назначает имя сотрудника
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__name = data

    def set_job_position(self, data: str):
        """
        Назначает занимаеиую должность сотрудника
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__job_position = data

    def set_id_employee(self, data: int):
        """
        Назначает ID сотрудника
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        self.__id_employee = data

    def add_contact_info(self, data: ContactInfo):
        """
        Добавляет контактную информацию о сотруднике
        :param data: Пренимает контактную информацию о сотруднике
        :return: None
        """
        if not isinstance(data, ContactInfo):
            raise TypeError('Получен не верный тип данных, ожидались данные типа ContactInfo')
        self.__contact_info.append(data)

    def remove_contact_info(self, data: ContactInfo):
        """
        Добавляет контактную информацию о сотруднике
        :param data: Пренимает контактную информацию о сотруднике
        :return: None
        """
        if not isinstance(data, ContactInfo):
            raise TypeError('Получен не верный тип данных, ожидались данные типа ContactInfo')
        self.__contact_info.remove(data)

    def __str__(self):
        """
        :return: Возвращает строковое значение объекта ContactInfo
        """
        return (f'Имя сотрудника: {self.__name}\n'
                f'Занимаемая должность: {self.__job_position}\n'
                f'ID сотрудника: {self.__id_employee}\n'
                f'Контактная информация: {self.__contact_info}\n')

