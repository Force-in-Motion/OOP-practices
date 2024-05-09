# class Patient:
#
#     def __init__(self, full_name: str, age: int, disease: str):
#         """
#         Формирует шаблон объекта Patient
#         :param full_name: Пренимает ФИО пациента
#         :param age: Пренимает возраст пациента
#         :param disease: Пренимает заболевание пациента
#         """
#         self.full_name = full_name
#         self.age = age
#         self.disease = disease
#
#
#     def makes_an_appointment(self, date: str):
#         """
#         Выводит уведомление о записи на прием к врачу на указанную дату
#         :param date: Пренимает дату записи на прием
#         :return:
#         """
#         print(f'Вы успешно записаны на прием на следующую дату: {date}\n')
#
#
#     def print_patient_info(self):
#         print('Данные пациента:\n'
#               f'ФИО пациента: {self.full_name}\n'
#               f'Возраст пациента: {self.age}\n'
#               f'Текущее заболевание пациента: {self.disease}\n')
#
# valera = Patient('Петров Иван Иванович', 42, 'Понос')
#
# valera.makes_an_appointment('24. 12. 1807')
# valera.print_patient_info()


# class TouristSpot:
#
#     def __init__(self, name_place: str, country: str, type_of_attraction: str):
#         """
#          Формирует шаблон объекта TouristSpot
#         :param name_place: Пренимает название места
#         :param country: Пренимает страну расположения
#         :param type_of_attraction: Пренимает тип достопримечательности
#         """
#         self.name_place = name_place
#         self.country = country
#         self.type_of_attraction = type_of_attraction
#
#
#     def visiting_the_place(self, name: str):
#         """
#         Выводит сообщение о посещении посетителем места
#         :param name:
#         :return:
#         """
#         print(f'Турист {name} посетил {self.name_place}, расположенню в {self.country}\n')
#
#
#     def print_info_name_place(self):
#         """
#         Выводит информацию о туристическом месте
#         :return:
#         """
#         print(f'Название места: {self.name_place}\n'
#               f'Страна расположения: {self.country}\n'
#               f'Тип достопримечательности: {self.type_of_attraction}')
#
#
# venecia = TouristSpot('Венеция', 'Италия', 'Венециансктй театр')
# venecia.visiting_the_place('Аркадий')
# venecia.print_info_name_place()


class ModelWindow:

    def __init__(self, name_window: str, coordinates_left_angle: float, horizontal_size: float, verticals_size: float, color_window: str, state_visibility: str, state_frame: str):
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
