import math

class Patient:

    def __init__(self, full_name: str, age: int, disease: str):
        """
        Формирует шаблон объекта Patient
        :param full_name: Пренимает ФИО пациента
        :param age: Пренимает возраст пациента
        :param disease: Пренимает заболевание пациента
        """
        self.full_name = full_name
        self.age = age
        self.disease = disease


    def makes_an_appointment(self, date: str):
        """
        Выводит уведомление о записи на прием к врачу на указанную дату
        :param date: Пренимает дату записи на прием
        :return:
        """
        print(f'Вы успешно записаны на прием на следующую дату: {date}\n')


    def print_patient_info(self):
        print('Данные пациента:\n'
              f'ФИО пациента: {self.full_name}\n'
              f'Возраст пациента: {self.age}\n'
              f'Текущее заболевание пациента: {self.disease}\n')



class TouristSpot:

    def __init__(self, name_place: str, country: str, type_of_attraction: str):
        """
         Формирует шаблон объекта TouristSpot
        :param name_place: Пренимает название места
        :param country: Пренимает страну расположения
        :param type_of_attraction: Пренимает тип достопримечательности
        """
        self.name_place = name_place
        self.country = country
        self.type_of_attraction = type_of_attraction


    def visiting_the_place(self, name: str):
        """
        Выводит сообщение о посещении посетителем места
        :param name:
        :return:
        """
        print(f'Турист {name} посетил {self.name_place}, расположенню в {self.country}\n')


    def print_info_name_place(self):
        """
        Выводит информацию о туристическом месте
        :return:
        """
        print(f'Название места: {self.name_place}\n'
              f'Страна расположения: {self.country}\n'
              f'Тип достопримечательности: {self.type_of_attraction}')


class ModelWindow:

    name_window: str
    coordinates_left_angle: int
    color_window: str
    state_visibility: str
    state_frame: str
    horizontal_size = 1980
    vertical_size = 1080

    def __init__(self, name_window: str, coordinates_left_angle: int, color_window: str, state_visibility: str, state_frame: str, horizontal_size=1980, verticals_size=1080):
        """
        Формирует шаблон объекта ModelWindow
        :param name_window: Пренимает заголовок окна
        :param coordinates_left_angle: Пренимает координаты левого угла
        :param horizontal_size: Пренимает размер по горизонтали
        :param verticals_size: Пренимает размер по вертикали
        :param color_window: Пренимает цвет окна
        :param state_visibility: Пренимает состояние: “видимое/невидимое”
        :param state_frame: Пренимает состояние: “с рамкой/без рамки”
        """

        self.name_window = name_window
        self.coordinates_left_angle = coordinates_left_angle
        self.horizontal_size = horizontal_size
        self.verticals_size = verticals_size
        self.color_window = color_window
        self.state_visibility = state_visibility
        self.state_frame = state_frame

    def movement_window_for_horizontal(self, new_x, new_y):
        """
        Передвигает окно по горизонтали и по вертикали
        :return:
        """
        if not self.horizontal_size <= ModelWindow.horizontal_size and self.verticals_size <= ModelWindow.vertical_size:
            print('Введено недопустимое значение, максимальное разрешение экрана 1960х1080 введите другое значение')
        else:
            self.horizontal_size = new_x
            self.verticals_size = new_y


    def height_change_or_width(self, new_horizontal, new_vertical):
        """
        Изменяет высоту окна или его ширину и высоту
        :return:
        """
        if not self.horizontal_size <= ModelWindow.horizontal_size and self.verticals_size <= ModelWindow.vertical_size:
            print('Введено недопустимое значение, максимальное разрешение экрана 1960х1080 введите другое значение')
        else:
            self.horizontal_size = new_horizontal
            self.verticals_size = new_vertical


    def change_color(self, new_color):
        """
        Изменяет цвет окна
        :return:
        """
        self.color_window = new_color


    def change_state_visibility(self, new_state_visibility, new_state_frame):
        """
        Изменяет состояние: “видимое/невидимое” и “с рамкой/без рамки”
        :return:
        """
        self.state_visibility = new_state_visibility
        self.state_frame = new_state_frame


    def displays_status(self):
        """
        Выводит состояние: “с рамкой/без рамки” и “видимое/невидимое”
        :return:
        """
        print(f'Состояние видимости: {self.state_visibility}\n'
              f'Наличие рамки: {self.state_frame}\n')


    def __str__(self):
        return (f'Текущее состояние окна:\n'
                f'Заголовок окна: {self.name_window}\n'
                f'Координаты левого верхнего угла: {self.coordinates_left_angle}\n'
                f'Размер по горизонтали: {self.horizontal_size}\n'
                f'Размер по вертикали: {self.verticals_size}\n'
                f'Цвет окна: {self.color_window}\n'
                f'Состояние “видимое/невидимое”: {self.state_visibility}\n'
                f'Состояние “с рамкой/без рамки”: {self.state_frame}')


class ArrayUtils:

    @staticmethod
    def sum_elems(lst: list):
        """
        Выполняет сложение элементов массива
        :param lst: Пренимает массив
        :return: Возвращает Результат сложения элементов массива
        """
        sum = 0
        for elem in lst:
            sum += elem
        return sum


    @staticmethod
    def mult_elems(lst: list):
        """
        Выполняет умножение элементов массива
        :param lst: Пренимает массив
        :return: Возвращает Результат умножения элементов массива
        """
        mult = 1
        for elem in lst:
            mult *= elem
        return mult


    @staticmethod
    def invers_elems(lst: list):
        """
        Выполняет инверсию массива
        :param lst: Пренимает массив
        :return: Возвращает перевернутый массив
        """
        lst = lst[::-1]
        return lst


    @staticmethod
    def max_elem(lst: list):
        """
        Находит максимальный элемент масива
        :param lst: Пренимает массив
        :return: Возвращает максимальный элемент массива
        """
        max_elem = 0
        for elem in lst:
            if elem > max_elem:
                max_elem = elem
        return max_elem


    @staticmethod
    def min_elem(lst: list):
        """
        Находит минимальный элемент масива
        :param lst: Пренимает массив
        :return: Возвращает минимальный элемент массива
        """
        min_elem = 99999999999999999999999
        for elem in lst:
            if elem < min_elem:
                min_elem = elem
        return min_elem


class Vector:

    x = float
    y = float
    z = float

    def __init__(self, x: float, y: float, z: float):
        """
        Формирует шаблон объекта
        :param x: Пренимает координату x
        :param y: Пренимает координату y
        :param z: Пренимает координату z
        """
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_x = self.x * other
            new_y = self.y * other
            new_z = self.z * other
            return Vector(new_x, new_y, new_z)

        if isinstance(self, Vector) or isinstance(other, Vector):
            new_x = self.y * other.z - self.z * other.y
            new_y = self.z * other.x - self.x * other.z
            new_z = self.x * other.y - self.y * other.x
            return Vector(new_x, new_y, new_z)

    @staticmethod
    def find_scalar_mult(vec_a, vec_b):
        scalar_mult = vec_a.x * vec_b.x + vec_a.y * vec_b.y + vec_a.z * vec_b.z
        return scalar_mult

    @staticmethod
    def find_norm_lenght_vector(self):
        lenght_vector = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return lenght_vector

    def __str__(self):
        return f'Результат текущих вычислений: {self.x, self.y, self.z}'


class GeometryUtils:

    @staticmethod
    def find_area_circle(radius):
        """
        Вычисляет площадь круга
        :param radius: Пренимает радиус
        :return: Возвращает результат
        """
        return math.pi * (radius ** 2)

    @staticmethod
    def find_perimetr_circle(radius):
        """
        Вычисляет периметр круга
        :param radius: Пренимает радиус
        :return: Возвращает результат
        """
        return 2 * math.pi * radius

    @staticmethod
    def find_area_rectangle(length, width):
        """
        Вычисляет площадь прямоугольника
        :param length: Пренимает длину
        :param width: Пренимает ширину
        :return: Возвращает результат
        """
        return length * width

    @staticmethod
    def find_perimetr_rectangle(length, width):
        """
        Вычисляет периметр прямоугольника
        :param length: Пренимает длину
        :param width: Пренимает ширину
        :return: Возвращает результат
        """
        return 2 * (length + width)

    @staticmethod
    def find_area_triangle(a, b, c):
        """
        Вычисляет площадь треугольника
        :return: Возвращает результат
        """
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Program:
    @staticmethod
    def main():
        """
        Запускает программу
        :return:
        """
        valera = Patient('Петров Иван Иванович', 42, 'Понос')
        valera.makes_an_appointment('24. 12. 1807')
        valera.print_patient_info()

        venecia = TouristSpot('Венеция', 'Италия', 'Венециансктй театр')
        venecia.visiting_the_place('Аркадий')
        venecia.print_info_name_place()

        window = ModelWindow('Ананас', '120', 'Grey', 'Не видимое', 'Без рамки')
        window.movement_window_for_horizontal(250, 480)
        window.height_change_or_width(1840, 920)
        window.change_color('Yelow')
        window.change_state_visibility('Видимое', 'С рамкой')
        window.displays_status()
        print(window)

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(f'Сумма элементов массива: {ArrayUtils.sum_elems(lst)}\n'
              f'Произведение элементов массива: {ArrayUtils.mult_elems(lst)}\n'
              f'Инверсия элементов массива: {ArrayUtils.invers_elems(lst)}\n'
              f'Максимальный элемент массива: {ArrayUtils.max_elem(lst)}\n'
              f'Минимальный элемент массива: {ArrayUtils.min_elem(lst)}')

Program.main()