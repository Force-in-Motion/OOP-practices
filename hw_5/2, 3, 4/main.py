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
        return (f'Название книги: {self.__title}'
                f'Автор книги: {self.__author}'
                f'Год публикации книги: {self.__year_publishing}'
                f'ID книги: {self.__id_book}'
                f'Список жанров книги: {self.__list_genre}')




class Genre:
    pass