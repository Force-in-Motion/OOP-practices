
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
        print(f'{self.type} с именем {self.name} издает звук: {self.sound}\n')

    def print_info_animal(self):
        """
        Выводит в консоль всю информацию о животном в созданном объекте на базе класса Animal
        :return:
        """
        print(f'Информационный блок о созданном вами животном :'
              f'\nВид животного : {self.type}'
              f'\nИмя животного : {self.name}'
              f'\nВозраст животного: {self.age}'
              f'\nЗвук который издает животное: {self.sound}\n')


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

    def open_page(self, number_page: int):
        """
        Выполняет проверки и если они пройдены выводит строку- открылась страница или нет
        :return:
        """
        if not isinstance(number_page, int):
            print('Вы ввели недопустимый тип данных, введите число')

        if number_page <= self.count_pages and number_page > 0:
            print('Страница в вашей книге найдена и открыта\n')
        else:
            print('Номер указанной страницы в вашей книге отсутствует\n')


    def print_book_info(self):
        """
        Выводит в консоль всю информацию о книге в созданном объекте на базе класса Book
        :return:
        """
        print(f'Информационный блок о вашей книге :'
              f'\nНазвание книги: {self.name}'
              f'\nАвтор книги: {self.author}'
              f'\nКоличество страниц: {self.count_pages}\n')


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
        print('Самолет взлетел!\n')


    def plane_landing(self):
        """
        Выводит на консоль посадку самолета если он сел
        :return:
        """
        print('Самолет приземлился!\n')


    def height_change(self, altitude):
        """
        Выводит на консоль изменение высоты самолета если она изменилась
        :return:
        """

        self.current_altitude = altitude

    def speed_change(self, speed):
        """
        Выводит на консоль изменение скорости самолета если она изменилась
        :return:
        """

        self.current_speed = speed


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


class MusicAlbum:

    def __init__(self, executor: str, name_albom: str, genre: str, track_list: list ):
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


    def add_track(self, track: str):
        """
        Добавляет трек в список треков
        :param track: Пренимает название трека
        :return:
        """
        self.track_list.append(track)


    def dell_track(self, track: str):
        """
        Удаляет трек из списка треков
        :param track: Пренимает название трека
        :return:
        """
        if track in self.track_list:
            self.track_list.remove(track)


    def reproduces_track(self, track: str):
        """
        Воспроизводит трек, если он есть в списке
        :param track: Пренимает название трека
        :return:
        """
        if track in self.track_list:
            print(f'Воспроизведение трека {track}....\n')


    def print_albom_info(self):
        """
        Выводит в консоль всю информацию о музыкальном альбомее в созданном объекте на базе класса MusicAlbum
        :return:
        """
        print(f'Информационный блок о вашем музыкальном альбоме :'
              f'\nИсполнитель: {self.executor}'
              f'\nЖанр музыки: {self.genre}'
              f'\nНазвание альбома: {self.name_albom}'
              f'\nСписок треков: {self.track_list}\n')



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
        air_plane.speed_change(500)
        air_plane.height_change(1200)
        air_plane.plane_landing()
        air_plane.print_PassengerPlane_info()
#============================================================================================

        muz_albom = MusicAlbum('БИ 2', 'Горизонт событий', 'Рок', ['Летчик', 'Ананас', 'Кручу верчу', 'Веник'])

        muz_albom.print_albom_info()
        muz_albom.add_track('Верона')
        muz_albom.dell_track('Ананас')
        muz_albom.reproduces_track('Веник')
        muz_albom.print_albom_info()

Programm.main()
