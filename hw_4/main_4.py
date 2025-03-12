from __future__ import annotations
class Wizard:

    name: str
    faculty: str
    lvl_magic_power: int
    status: bool
    list_skills: list = None

    def __init__(self, name: str, faculty: str, lvl_magic_power: int, status: bool, list_skills: list = None):
        """
        Формирует шаблон объекта Wizard
        :param name: Пренимает имя волшебника
        :param faculty: Пренимает название факультета волшебника
        :param lvl_magic_power: Пренимает уровень магической силы волшебника
        :param status: Пренимает статус волшебника ( в Хогвартсе или выпущен )
        :param list_skills: Пренимает список известных волшебнику заклинаний
        """
        self.__name = name
        self.__faculty = faculty
        self.__lvl_magic_power = lvl_magic_power
        if list_skills is None:
            self.__list_skills = []
        else:
            self.__list_skills = list_skills
        self.__status = status

    def get_name(self):
        """
        :return: Возвращает имя волшебника
        """
        return self.__name

    def get_house(self):
        """
        :return:  Возвращает факультет волшебника
        """
        return self.__faculty

    def get_magic_level(self):
        """
        :return: Возвращает уровень магической силы волшебника
        """
        return self.__lvl_magic_power

    def get_spells(self):
        """
        :return: Возвращает список известных заклинаний волшебника
        """
        return self.__list_skills

    def get_status(self):
        """
        :return: Возвращает текущий статус волшебника
        """
        return self.__status

    def set_house(self, data: str):
        """
        Устанавливает факультет волшебника
        :param data: Пренимает новое название факультета в виде строки
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        else:
            self.__faculty = data

    def set_magic_level(self, data: int):
        """
        Устанавливает уровень магической силы
        :param data: Пренимает новое значение магической силы волшебника
        :return: None
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')
        if data < 0:
            raise ValueError('Получено не верное значение, уровень магической силы не может быть меньше нуля')
        else:
            self.__lvl_magic_power = data

    def set_status(self, data: bool):
        """
        Устанавливает текущий статус волшебника
        :return: None
        """
        if not isinstance(data, bool):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        if data:
            self.__status = 'В Хогвартсе'
        else:
            self.__status = 'Выпущен'

    def add_spell(self, data: Spell):
        """
        Добавляет заклинание в список известных
        :param data: Пренимает новое заклинание
        :return:
        """
        if not isinstance(data, Spell):
            raise TypeError('Получен не верный тип данных, ожидались данные типа Spell')
        else:
            self.__list_skills.append(data)

    def remove_spell(self, data: Spell):
        """
        Удаляет заклинание из списока известных
        :param data: Пренимает новое заклинание
        :return:
        """
        if not isinstance(data, Spell):
            raise TypeError('Получен не верный тип данных, ожидались данные типа Spell')
        else:
            self.__list_skills.remove(data)

    def increase_magic_level(self, data: int):
        """
        Увеличивает увеличивает уровень магической силы на заданное значение
        :param data: Пренимает новое значение силы
        :return:
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')
        if data < 0:
            raise ValueError('Получено не верное значение, уровень магической силы не может быть меньше нуля')
        else:
            self.__lvl_magic_power += data

    def __str__(self):
        return (f'Имя волшебника: {self.__name}\n'
                f'Факультет волшебника:{self.__faculty}\n'
                f'Уровень магической силы волшебника: {self.__lvl_magic_power}\n'
                f'Список известных заклинаний волшебника: {self.__list_skills}\n'
                f'В Хогвартсе волшебник или выпущен: {self.__status}\n')


class Spell:

    name_spell: str
    lvl_complexity: int
    type_spell: str
    description: str

    def __init__(self, name_spell: str, lvl_complexity: int, type_spell: str, description: str):
        """
        Формирует шаблон объекта Spell
        :param name_spell: Пренимает название заклинания
        :param lvl_complexity: Пренимает уровень сложности от 1 до 10
        :param type_spell: Пренимает тип заклинания (боевое, лечебное и т.д.)
        :param description: Пренимает описание заклинания
        """
        self.__name_spell = name_spell
        self.__lvl_complexity = lvl_complexity
        self.__type_spell = type_spell
        self.__description = description

    def get_name_spell(self):
        """
        :return: Возвращает название заклинания
        """
        return self.__name_spell

    def get_lvl_complexity(self):
        """
        :return: Возвращает уровень сложности заклинания от 1 до 10
        """
        return self.__lvl_complexity

    def get_type_spell(self):
        """
        :return: Возвращает тип заклинания (боевое, лечебное и т.д.)
        """
        return self.__type_spell

    def get_description(self):
        """
        :return: Возвращает описание заклинания
        """
        return self.__description

    def set_name_spell(self, data: str):
        """
        Устанавливает новое название заклинания
        :param data: Пренимает новое название
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        else:
            self.__name_spell = data

    def set_lvl_complexity(self, data: int):
        """
        Устанавливает новый уровень сложности заклинания
        :param data: Пренимает новый уровень сложности заклинания
        :return:
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, целое число от 1 до 10')
        else:
            self.__lvl_complexity = data


    def set_type_spell(self, data: str):
        """
        Устанавливает новый тип заклинания (боевое, лечебное и т.д.)
        :param data: Пренимает новый тип заклинания
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        else:
            self.__type_spell = data

    def set_description(self, data: str):
        """
        Устанавливает новое описание заклинания
        :param data: Пренимает новое описание заклинания
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        else:
            self.__description = data

    def __str__(self):
        return (f'\nНазвание заклинания: {self.__name_spell}\n'
                f'Уровень сложности: { self.__lvl_complexity}\n'
                f'Тип заклинания: {self.__type_spell}\n'
                f'Описание заклинания: {self.__description}')



class Employee:

    name: str
    job_title: str
    department: str
    salary: float
    work_experience: int
    list_pogects: list

    def __init__(self, name: str, job_title: str, department: str, salary: float, work_experience: int, list_pogects: list):
        """
        Формирует шаблон объекта Employee
        :param name: Пренимает имя сотрудника
        :param job_title: Пренимает должность сотрудника
        :param department: Пренимает отдел сотрудника
        :param salary: Пренимает зарплату сотрудника
        :param work_experience: Пренимает стаж работы сотрудника в годах
        :param list_pogects: Пренимает список выполненных проектов сотрудника
        """
        self.__name = name
        self.__job_title = job_title
        self.__department = department
        self.__salary = salary
        self.__work_experience = work_experience
        self.__list_pogects = list_pogects

    def get_name(self):
        """
        :return: Возвращает имя сотрудника
        """
        return self.__name

    def get_job_title(self):
        """
        :return: Возвращает должность сотрудника
        """
        return self.__job_title

    def get_department(self):
        """
        :return: Возвращает отдел сотрудника
        """
        return self.__department

    def get_salary(self):
        """
        :return: Возвращает зарплату сотрудника
        """
        return self.__salary

    def get_work_experience(self):
        """
        :return: Возвращает стаж работы сотрудника в годах
        """
        return self.__work_experience

    def get_list_pogects(self):
        """
        :return: Возвращает список выполненных проектов сотрудника
        """
        return self.__list_pogects


    def set_name(self, data: str):
        """
        Устанавливает новое имя сотрудника
        :param data: Пренимает новое имя сотрудника
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        else:
            self.__name = data

    def set_job_title(self, data: str):
        """
        Устанавливает новую должность сотрудника
        :param data: Пренимает новую должность сотрудника
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        else:
            self.__job_title = data


    def set_department(self, data: str):
        """
        Устанавливает новый отдел сотрудника
        :param data: Пренимает новый отдел сотрудника
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')
        else:
            self.__department = data

    def set_work_experience(self, data: int):
        """
        Устанавливает стаж работы сотрудника в годах
        :param data: Пренимает стаж работы сотрудника в годах
        :return:
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')
        else:
            self.__work_experience = data

    def add_salary(self, data: float or int):
        """
        Увеличивает зарплату сотрудника
        :param data: Пренимает новую зарплату сотрудника
        :return:
        """
        if not isinstance(data, float or int):
            raise TypeError('Получен не верный тип данных, ожидалось число')
        if data < 0:
            raise ValueError('Получено не верное значение, зарплата может быть увеличена если введеное значение больше нуля')
        else:
            self.__salary += data

    def add_elem_in_list_pogects(self, data: str):
        """
        Добавляет новый проект в список выполненных сотрудником
        :param data: Пренимает новый проект
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')

        else:
            self.__list_pogects.append(data)

    def remove_elem_in_list_pogects(self, data: str):
        """
        Удаляет проект из списока выполненных сотрудником
        :param data: Пренимает  проект
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')

        if len(self.__list_pogects) == 0:
            raise ValueError('Список достижений пуст, удалять нечего')

        else:
            self.__list_pogects.remove(data)

    def __str__(self):
        return (f'Имя сотрудника: {self.__name}\n'
                f'Должность сотрудника: {self.__job_title}\n'
                f'Отдел сотрудника: {self.__department}\n'
                f'Зарплата сотрудника: {self.__salary}\n'
                f'Стаж работы сотрудника: {self.__work_experience}\n'
                f'Список выполненных проектов сотрудника: {self.__list_pogects}\n')


class Robot:

    number: int
    model: str or int
    current_task: str
    lvl_charge: int
    state: bool

    def __init__(self, number: int, model: str or int, current_task: str, lvl_charge: int, state: bool):
        """
        Формирует шаблон объекта Robot
        :param number: Пренимает серийный номер
        :param model: Пренимает модель
        :param current_task: Пренимает текущую задачу
        :param lvl_charge: Пренимает уровень заряда батареи
        :param state: Пренимает состояние (в работе или на перерыве)
        """
        self.__number = number
        self.__model = model
        self.__current_task = current_task
        self.__lvl_charge = lvl_charge
        self.__state = state

    def get_number(self):
        """
        :return: Возвращает серийный номер
        """
        return self.__number

    def get_model(self):
        """
        :return: Возвращает модель
        """
        return self.__model

    def get_current_task(self):
        """
        :return: Возвращает текущую задачу
        """
        return self.__current_task

    def get_lvl_charge(self):
        """
        :return: Возвращает уровень заряда батареи
        """
        return self.__lvl_charge

    def get_state(self):
        """
        :return: Возвращает состояние (в работе или на перерыве)
        """
        return self.__state

    def set_current_task(self, date: str):
        """
        Назначает новую задачу
        :return: None
        """
        if not isinstance(date, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')

        else:
            self.__current_task = date

    def set_lvl_charge(self, data: int):
        """
        Изменяет уровень заряда батареи
        :return: None
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')

        else:
            self.__lvl_charge = data

    def set_state(self, data: bool):
        """
        Изменяет состояние (в работе или на перерыве)
        :return: None
        """
        if not isinstance(data, bool):
            raise TypeError('Получен не верный тип данных, ожидалось булевое значение')

        if data:
            self.__state = 'В работе'

        else:
            self.__state = 'На перерыве'

    def __str__(self):
        return (f'Серийный номер: {self.__number}\n'
                f'Модель: {self.__model}\n'
                f'Текущая задача: {self.__current_task}\n'
                f'Уровень заряда батареи: {self.__lvl_charge}\n'
                f'Состояние: {self.__state}\n')


class Athlete:

    name: str
    age: int
    sport: str
    list_of_achievements: list = None
    status: bool

    def __init__(self, name: str, age: int, sport: str, status: bool, list_of_achievements: list = None):
        """
        Формирует шаблон класса Athlete
        :param name: Пренимает имя спортсмена
        :param age: Пренимает возраст спортсмена
        :param sport: Пренимает вид спорта спортсмена
        :param status: Пренимает статус спортсмена (активен или на пенсии)
        :param list_of_achievements: Пренимает список достижений спортсмена
        """
        self.__name = name
        self.__age = age
        self.__sport = sport
        self.__status = status
        if list_of_achievements is None:
            self.__list_of_achievements = []
        else:
            self.__list_of_achievements = list_of_achievements


    def get_name(self):
        """
        :return: Возвращает имя спортсмена
        """
        return self.__name

    def get_age(self):
        """
        :return: Возвращает возраст спортсмена
        """
        return self.__age

    def get_sport(self):
        """
        :return: Возвращает вид спорта спортсмена
        """
        return self.__sport

    def get_status(self):
        """
        :return: Возвращает статус спортсмена (активен или на пенсии)
        """
        return self.__status

    def get_list_of_achievements(self):
        """
        :return: Возвращает список достижений спортсмена
        """
        return self.__list_of_achievements


    def set_name(self, data: str):
        """
        Назначает новое имя спортсмена
        :param data: Пренимает новое имя
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')

        else:
            self.__name = data

    def set_age(self, data: int):
        """
        Назначает новое имя спортсмена
        :param data: Пренимает новое имя
        :return:
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')

        else:
            self.__age = data

    def set_sport(self, data: str):
        """
        Назначает новое имя спортсмена
        :param data: Пренимает новое имя
        :return:
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')

        else:
            self.__sport = data

    def set_status(self, data: bool):
        """
        Назначает новое имя спортсмена
        :param data: Пренимает новое имя
        :return:
        """
        if not isinstance(data, bool):
            raise TypeError('Получен не верный тип данных, ожидалось булевое значение')

        if data:
            self.__status = 'Активен'

        else:
            self.__status = 'На пенсии'

    def add_achievements_in_list(self, data: Achievement):
        """
        Добавляет новое достижение в список, если оно соответствует условиям
        :param data: Пренимает новое достижение
        :return:
        """
        if not isinstance(data, Achievement):
            raise TypeError('Получен не верный тип данных, ожидалось значение типа Achievement')

        else:
            self.__list_of_achievements.append(data)

    def remove_achievements_in_list(self, data: Achievement):
        """
        Удаляет новое достижение в список, если оно соответствует условиям
        :param data: Пренимает новое достижение
        :return:
        """
        if not isinstance(data, Achievement):
            raise TypeError('Получен не верный тип данных, ожидалось значение типа Achievement')

        if len(self.__list_of_achievements) == 0:
            raise ValueError('Список достижений пуст, удалять нечего')

        else:
            self.__list_of_achievements.remove(data)

    def __str__(self):
        return (f'Имя спортсмена: {self.__name}\n'
                f'Возраст спортсмена: {self.__age}\n'
                f'Вид спорта: {self.__sport}\n'
                f'Статус спортсмена: {self.__status}\n'
                f'Список достижений спортсмена: {self.__list_of_achievements}\n')


class Achievement:

    name: str
    year_of_issue: int

    def __init__(self, name: str, year_of_issue: int):
        """
        Формирует шаблон объекта Achievement
        :param name: Пренимает название достижения
        :param year_of_issue: Пренимает год получения достижения
        """
        self.__name = name
        self.__year_of_issue = year_of_issue

    def __str__(self):
        return (f'Название достижения: {self.__name}\n'
                f'Год получения достижения: {self.__year_of_issue}\n')



class Program:

    @staticmethod
    def main():
# ================================= Spell ==============================================

        aoe_fire = Spell('Колдунство огня', 28, 'Атакующее', 'Обрушивает на указанную площадь огненный ливень, поджигая все вокруг\n')

        corrozia = Spell('Порча', 28, 'Атакующее', 'Проклинает цель, которая получает постепенный урон с течением времени\n')

        mass_heall = Spell('Массовое лечение', 78, 'Лечащее', 'Лечит все цели в указанной области\n')

        print(aoe_fire, corrozia, mass_heall)

# ================================= Wizard =============================================

        wizard = Wizard('Колдун Василий', 'Некромантия', 80, True, ['Лечение жабами', 'Воскрешение трупов'])

        wizard.set_status(True)

        wizard.add_spell(aoe_fire)

        wizard.add_spell(corrozia)

        print(wizard)

        wizard.set_status(False)

        wizard.add_spell(mass_heall)

        wizard.remove_spell(corrozia)

        wizard.increase_magic_level(20)

        print(wizard)

# ================================= Employee ===========================================

        valera = Employee('Валера', 'Коллектор', 'Коллекторский отдел', 25.500, 20, ['Отжал у банкира долг', 'Наказал работягу'])

        print(valera)

        valera.add_elem_in_list_pogects('Натянул потолки')

        valera.add_salary(45.2)

        print(valera)

# ================================= Robot ==============================================

        robot_natasha = Robot(987, 'Домработница', 'Помыть посуду', 58, True)

        print(robot_natasha)

        robot_natasha.set_current_task('Пропылесосить')

        robot_natasha.set_lvl_charge(98)

        robot_natasha.set_state(False)

        print(robot_natasha)

# ================================= Achievement ============================================

        achivment = Achievement('Нокаутировал Тайсона', 1998)

        print(achivment)
# ================================= Athlete ============================================

        jorik = Athlete('Жорик', 45, 'Бокс', False, ['ЗМС', 'Победа на чемпионате россии', 'Победа на кубке золотой перчатки'])

        jorik.add_achievements_in_list(achivment)

        jorik.set_status(True)

        print(jorik)

# ======================================================================================

spell = Achievement('gggg', 1234)
print(spell.__str__())
print(Achievement.__str__(spell))
