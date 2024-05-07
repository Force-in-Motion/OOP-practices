
class Animal:
    def __init__(self, name: str, type: str, age: int, sound: str):
        """
        Формирует шаблон объекта Animal
        :param name: Пренимает имя животного
        :param type: Пренимает вид животного
        :param age: Пренимает возраст животного
        :param sound: Пренимает звук, создаваемый животным
        """
        self.name = name
        self.type = type
        self.age = age
        self.sound = sound

    def print_sound_animal(self):
        """
        Выводит в консоль строку с принятым иенем животного его типом и звуком который оно издает
        :return:
        """
        print(f'{self.type} с именем {self.name} издает звук: {self.sound}')
        print()

    def print_info_animal(self):
        """
        Выводит в консоль всю информацию о животном в созданном объекте на базе класса Animal
        :return:
        """
        print(f'Информационный блок о созданном вами животном :'
              f'\nВид животного : {self.type}'
              f'\nИмя животного : {self.name}'
              f'\nВозраст животного: {self.age}'
              f'\nЗвук который издает животное: {self.sound}')
        print()


dog = Animal('Шнырь', 'Пес', 7, 'Рррррааааааввв Рррррааааааввв')

dog.print_info_animal()
dog.print_sound_animal()


class Book:

    def __init__(self, name: str, author: str, count_pages: int):
        """
        Формирует шаблон объекта Book
        :param name: Пренимает название книги
        :param author: Пренимает автора книги
        :param count_pages: Пренимает количество страниц книги
        """
        self.name = name
        self.author = author
        self.count_pages = count_pages

    def open_page(self):
        """
        Выполняет проверки и если они пройдены выводит строку- открылась страница или нет
        :return:
        """
        number_page = int(input('Введите номер страницы, которую требуется открыть >> '))

        if number_page <= self.count_pages and number_page > 0:
            print('Страница в вашей книге найдена и открыта')
            print()
        else:
            print('Номер указанной страницы в вашей книге отсутствует')
            print()


    def print_book_info(self):
        """
        Выводит в консоль всю информацию о книге в созданном объекте на базе класса Book
        :return:
        """
        print(f'Информационный блок о вашей книге :'
              f'\nНазвание книги: {self.name}'
              f'\nАвтор книги: {self.author}'
              f'\nКоличество страниц: {self.count_pages}')
        print()

war_and_world = Book('Война и мир', 'Лев Толстой', 1300)
war_and_world.open_page()
war_and_world.print_book_info()


class PassengerPlane:

    def __init__(self, manufacturer: str, model: str, capacity: int, current_altitude: int, current_speed: int):
        """
        Формирует шаблон объекта PassengerPlane
        :param manufacturer: Пренимает название производителя
        :param model: Пренимает название модели
        :param capacity: Пренимает вместимость пассажиров
        :param current_altitude: Пренимает текущую высоту
        :param current_speed: Пренимает текущую скорость
        """
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.current_altitude = current_altitude
        self.current_speed = current_speed


    def takeoff(self):
        """
        Выводит на консоль взлет самолета если он взлетел
        :return:
        """
        altitude = int(input('Введите текущее значение высоты самолета >> '))
        if self.current_altitude < altitude:
            self.current_altitude = altitude
            print('Самолет взлетел!')
            print()
        else:
            print('Самолет находится на земле')
            print()

    def speed_change(self):
        """
        Выводит на консоль изменение скорости самолета если она изменилась
        :return:
        """
        speed = int(input('Введите текущее значение скорости самолета >> '))
        if self.current_speed < speed:
            self.current_speed = speed
            print('Самолет набирает скорость!')
            print()
        else:
            print('Самолет находится на земле')
            print()


    def height_change(self):
        """
        Выводит на консоль изменение высоты самолета если она изменилась
        :return:
        """
        altitude = int(input('Введите новое значение высоты самолета >> '))
        if self.current_altitude < altitude or self.current_altitude > altitude:
            self.current_altitude = altitude
            print('Самолет изменил высоту !')
            print()
        else:
            print('Самолет летит на той же высоте')
            print()


    def plane_landing(self):
        """
        Выводит на консоль посадку самолета если он сел
        :return:
        """
        altitude = int(input('Введите новое значение высоты самолета >> '))
        if altitude == 0:
            self.current_altitude = altitude
            print('Самолет приземлился!')
            print()
        elif self.current_altitude < altitude or self.current_altitude > altitude:
            self.current_altitude = altitude
            print('Самолет изменил высоту !')
            print()
        else:
            print('Самолет летит на той же высоте')
            print()


    def print_PassengerPlane_info(self):
        """
        Выводит в консоль всю информацию о пассажирском самолете в созданном объекте на базе класса PassengerPlane
        :return:
        """
        print(f'Информационный блок о вашем самолете :'
              f'\nПроизводитель самолета: {self.manufacturer}'
              f'\nМодель самолета: {self.model}'
              f'\nПассажировместимость самолета: {self.capacity}'
              f'\nТекущая высота самолета: {self.current_altitude}'
              f'\nТекущая скорость самолета: {self.current_speed}')
        print()


air_plane = PassengerPlane('Россия', 'Airbus A320NEO', 120, 0, 0)
air_plane.takeoff()
air_plane.speed_change()
air_plane.height_change()
air_plane.plane_landing()
air_plane.print_PassengerPlane_info()


class MusicAlbum:

    def __init__(self, executor: str, name_albom: str, genre: str, track_list: list):
        """
        Формирует шаблон объекта MusicAlbum
        :param executor: Пренимает исполнителя
        :param name_albom: Пренимает название альбома
        :param genre: Пренимает жанр
        :param track_list: Пренимает список треков
        """
        self.executor = executor
        self.name_albom = name_albom
        self.genre = genre
        self.track_list = track_list


    def add_track(self):
        """
        Добавляет в альбом песню
        :return:
        """
        track_list = []
        track = input('Введите название трека, который требуется добавить в альбом >>')
        track_list.append(track)
        print(f'Трек "{track}" был добавлен в альбом!')
        print()


    def dell_track(self):
        track = input('Введите название трека, который требуется удалить >>')

        text = f'В вашем альбоме нет трека с названием "{track}"'

        for i in self.track_list:
            if track == i:
                self.track_list.remove(i)
                text = f'Трек с названием "{track}" был успешно удален из вашего альбома'
        print(text)
        print()

    def reproduces_track(self):
        track = input('Введите название трека, который требуется воспроизвести >>')
        flag = False
        for i in self.track_list:
            if track == i:
                flag = True
                print('Воспроизведение песни....')
        if not flag:
                print('Указанный трек отсутствует в вашей коллекции')


    def print_albom_info(self):
        """
        Выводит в консоль всю информацию о музыкальном альбомее в созданном объекте на базе класса MusicAlbum
        :return:
        """
        print(f'Информационный блок о вашем музыкальном альбоме :'
              f'\nИсполнитель: {self.executor}'
              f'\nЖанр музыки: {self.genre}'
              f'\nНазвание альбома: {self.name_albom}'
              f'\nСписок треков: {self.track_list}')
        print()

muz_albom = MusicAlbum('БИ 2', 'Горизонт событий', 'Рок', 'Летчик, Ананас, Кручу верчу, Веник')
muz_albom.add_track()
muz_albom.dell_track()
muz_albom.reproduces_track()
muz_albom.print_albom_info()

class Programm:
    @staticmethod
    def main():

        dog = Animal('Шнырь', 'Пес', 7, 'Рррррааааааввв Рррррааааааввв')

        dog.print_info_animal()
        dog.print_sound_animal()
#============================================================================================

        war_and_world = Book('Война и мир', 'Лев Толстой', 1300)

        war_and_world.open_page()
        war_and_world.print_book_info()
#============================================================================================

        air_plane = PassengerPlane('Россия', 'Airbus A320NEO', 120, 0, 0)

        air_plane.takeoff()
        air_plane.speed_change()
        air_plane.height_change()
        air_plane.plane_landing()
        air_plane.print_PassengerPlane_info()
#============================================================================================

        muz_albom = MusicAlbum('БИ 2', 'Горизонт событий', 'Рок', ['Летчик', 'Ананас', 'Кручу верчу', 'Веник'])

        muz_albom.add_track()
        muz_albom.dell_track()
        muz_albom.reproduces_track()
        muz_albom.print_albom_info()

Programm.main()
