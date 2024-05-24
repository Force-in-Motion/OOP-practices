from __future__ import annotations


class Potion:

    name_potion: str
    ingredients = ['Чечевица', 'Усы пескова', 'Гвозди', 'Навоз']
    difficulty_preparation: int
    effect: str
    state_change: bool
    potion = []

    def __init__(self, name_potion: str,
                 difficulty_preparation: int,
                 effect: str, state_change: bool,
                 ingredients=['Чечевица', 'Усы пескова', 'Гвозди', 'Навоз'],
                 potion=[]):
       """
       Формирует объект по заданным параметрам
       :param name_potion: Пренимает название зелья
       :param ingredients: Пренимает Ингридиенты зелья
       :param difficulty_preparation: Пренимает сложность приготовления
       :param effect: Пренимает эффект зелья
       :param state_change: Пренимает состояние - "приготовлено/не приготовлено"
       """
       self.name_potion = name_potion
       self.ingredients = ingredients
       self.difficulty_preparation = difficulty_preparation
       self.effect = effect
       self.state_change = state_change
       self.potion = potion

    def set_add_ingridients(self, ingridient):
        """
        Добавляет ингридиент в список
        :param ingridient: Пренимает ингingridientидиент
        :return:
        """
        if isinstance(ingridient, str):
            self.ingredients.append(ingridient)
        else:
            raise TypeError('Введен не верный тип данных, требуется строка')

    def set_del_ingridients(self, ingridient):
        """
        Удаляет ингридиент из списка
        :param ingridient:
        :return:
        """
        if isinstance(ingridient, str):
            self.ingredients.remove(ingridient)
        else:
            raise TypeError('Введен не верный тип данных, требуется строка')


    def set_difficulty(self, data):
        """
        Изменяет сложность приготовления зелья
        :param data:
        :return:
        """
        if isinstance(data, int):
            self.difficulty_preparation = data
        else:
            raise TypeError('Введен не верный тип данных, требуется целое число от 1 до 10')

    def set_create_potion(self):
        """
        Готовит зелье из имеющихся ингридиентов
        :param ingredients: Пренимает список ингридиентов
        :return:
        """
        for item in self.ingredients:
            self.potion.append(item)


    def set_effect_potion(self, data):
        """
        Изменяет эффект зелья
        :return:
        """
        if isinstance(data, str):
            self.effect = data
        else:
            raise TypeError('Введен не верный тип данных, требуется строка')

    def get_state_potion(self):
        """
        :return: Возвращает текущее состояние зелья
        """
        return self.state_change


    def get_info_ingredients(self):
        """
        :return: Возвращает текущий список ингридиентов
        """
        return self.ingredients


    def __str__(self):
        return (f'Название зелья: {self.name_potion}\n'
                f'Список заготовленных ингридиентов: {self.ingredients}\n'
                f'Сложность приготовления: {self.difficulty_preparation}\n'
                f'Эффект зелья: {self.effect}\n'
                f'Текущее состояние зелья: {self.state_change}\n'
                f'Зелье содержит ингридиенты: {self.potion}\n')




class Library:

    name_bibliotec: str
    adres: str or int
    list_book: list[Book] = None
    list_users: list[User] = None

    def __init__(self, name_bibliotec: str, adres: str or int, list_book: list[Book] = None, list_users: list[User] = None, ):
        self.name_bibliotec = name_bibliotec
        self.adres = adres
        if list_book is None:
            self.list_book = []
        else:
            self.list_book = list_book
        if list_users is None:
            self.list_users = []
        else:
            self.list_users = list_users


    def add_book(self, book: Book):
        if isinstance(book, Book):
            if book not in self.list_book:
                self.list_book.append(book)
            else:
                raise ValueError('Указанный объект уже есть в списке')
        else:
            raise TypeError('Получен не верный тип данных')


    def remove_book(self, book: Book):
        if book in self.list_book:
            self.list_book.remove(book)
        else:
            raise ValueError('Указанный обьект отсутствует в списке')


    def register_user(self, user: User):
        if isinstance(user, User):
            if user not in self.list_users:
                self.list_users.append(user)
            else:
                raise ValueError('Указанный объект уже есть в списке')
        else:
            raise TypeError('Получен не верный тип данных')


    def issue_book(self, book: Book, user: User):
        """
        Выдает книгу пользователю если книга есть в наличии
        :param book: Пренимает название книги
        :param user: Пренимает текущего юзера
        :return:
        """
        if isinstance(book, Book) and isinstance(user, User):
            if book.state:
                book.set_current_user(user.name_user)
                user.list_taked_book.append(book)
                book.set_state(False)
            else:
                raise ValueError('Книги нет в наличии')
        else:
            raise TypeError('Получен не верный тип данных')


    def return_book(self, book: Book, user: User):
        """
        Возвращает книгу book от пользователя user обратно в библиотеку.
        :param book: Пренимает книгу
        :param user: Пренимает пользователя
        :return:
        """
        if isinstance(book, Book) and isinstance(user, User):
            if book in user.list_taked_book:
                user.list_taked_book.remove(book)
                self.list_book.append(book)
                book.set_state(True)
                book.set_current_user(None)
            else:
                raise ValueError('Кники нет в списке взятых пользователем')
        else:
            raise TypeError('Получен не верный тип данных')


    def __str__(self):
        return (f'Название библиотеки: {self.name_bibliotec}\n'
                f'Адрес библиотеки: {self.adres}\n'
                f'Список книг: {self.list_book}\n'
                f'Список пользователей: {self.list_users}\n')





class Book:

    name_book: str
    author: str
    year_publishing: int
    genre: str
    state: bool
    current_user: User = None

    def __init__(self, name_book: str, author: str, year_publishing: int, genre: str, state: bool, current_user: User = None):
        """
        Формирует шаблон объекта Book
        :param name_book: Пренимает название книги
        :param author: Пренимает автора книги
        :param year_publishing: Пренимает год издания
        :param genre: Пренимает жанр книги
        :param state: Пренимает состояние книги- в "наличии/выдана"
        :param current_user: Пренимает текущего пользователя
        """
        self.name_book = name_book
        self.author = author
        self.year_publishing = year_publishing
        self.genre = genre
        self.state = state
        self.current_user = current_user


    def set_state(self, data):
        """
        Изменяет состояние книли- "в наличии/выдана"
        :return:
        """
        if isinstance(data, bool):
            self.state = data
        else:
            raise TypeError('Получен не верный тип данных')


    def set_current_user(self, data):
        """
        Назначает текущего пользователя
        :param data:Пренимает данные в виде строки
        :return:
        """
        if self.current_user is not None:
            self.current_user = data


    def set_genre(self, data: str):
        """
        Изменяет жанр
        :param data: Пренимает данные в виде строки
        :return:
        """
        if isinstance(data, str):
            self.genre = data
        else:
            raise TypeError('Получен не верный тип данных')


    def get_state(self):
        """
        :return: Возвращает информацию о книге
        """
        return (f'Название: {self.name_book}\n'
                f'Автор: {self.author}\n'
                f'Текущий пользователь: {self.current_user}\n')


    def __str__(self):
        return (f'Название книги: {self.name_book}\n'
                f'Название автора: { self.author}\n'
                f'Год издания: {self.year_publishing}\n'
                f'Текущее состояние: :{self.state}\n'
                f'Жанр: {self.genre}\n'
                f'Текущий пользователь: {self.current_user}\n')


class User:

    name_user: str
    number_ticket: int
    list_taked_book: list[Book] = None

    def __init__(self, name_user: str, number_ticket: int, list_taked_book: list[Book] = None):
        """
        Формирует шаблон объекта User
        :param name_user: Пренимает имя пользователя
        :param number_ticket: Пренимает номер читательского билета
        :param list_taked_book: Пренимает список взятых книг
        """
        self.name_user = name_user
        self.number_ticket = number_ticket
        if list_taked_book is None:
            self.list_taked_book = []
        else:
            self.list_taked_book = list_taked_book


    def add_in_list_book(self, book: Book):
        """
        Добавляет книгу в список взятых
        :param book: Пренимает книгу
        :return:
        """
        if isinstance(book, Book):
            self.list_taked_book.append(book)
        else:
            raise TypeError('Получен не верный тип данных')


    def remove_book_from_list_book(self, book: Book):
        """
        Удаляет книгу из списка взятых
        :param book: Пренимает книгу
        :return:
        """
        if isinstance(book, Book):
            self.list_taked_book.remove(book)
        else:
            raise TypeError('Получен не верный тип данных')


    def get_status_list_book(self):
        """
        Возвращает текущий список взятых книг
        :return:
        """
        return f'Список взятых книг: {self.list_taked_book}'


    def __str__(self):
        return (f'Имя пользователя: {self.name_user}\n'
                f'Номер читательского билета: {self.number_ticket}\n'
                f'Список взятых книг: {self.list_taked_book}\n')



class Program:

    @staticmethod
    def main():
        potion = Potion('Зелье скорости', 10, 'Увеличение скорости бега', True)
        print(potion)
        potion.set_add_ingridients('Бычьи яйца', )
        potion.set_del_ingridients('Гвозди')
        potion.set_difficulty(8)
        potion.set_create_potion()
        potion.set_effect_potion('Уменьшение гравитации')
        potion.get_state_potion()
        potion.get_info_ingredients()
        print(potion)


        library = Library('Ботаническая', 'Твардовского 48')
        war_and_world = Book('Война и мир', 'Лев Толстой', 1958, 'Драмма', True)
        cheburek = Book('Чебурашка', 'Чехов', 1978, 'Боевик', True)
        valera = User('Валера', 98)
        gennadiy = User('Гена', 100)

        library.add_book(cheburek)
        library.add_book(war_and_world)
        library.register_user(valera)
        library.register_user(gennadiy)
        library.issue_book(war_and_world, valera)

        print(library)
        print(war_and_world)
        print(valera)


Program.main()
