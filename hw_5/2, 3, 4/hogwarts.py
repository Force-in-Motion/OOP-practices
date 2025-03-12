from __future__ import annotations
import random

class HogwartsStudent:

    __name: str
    __home_hogwards: str
    __mana: int
    __list_spells: list[Spell]

    def __init__(self, name: str,  home_hogwards: str, mana: int = 100, list_spells: list[Spell] = None):
        """
        Формирует шаблон объекта HogwartsStudent
        :param name: Пренимает название
        :param home_hogwards: Пренимает дом Хогвардса
        :param mana: Пренимает количество маны
        :param list_spells: Пренимает список изученных заклинаний
        """
        self.__name = name
        self.__home_hogwards = home_hogwards
        self.__mana = mana
        if list_spells is None:
            self.__list_spells = []
        else:
            self.__list_spells = list_spells

    def get_name(self) -> str:
        """
        :return: Возвращает название
        """
        return self.__name

    def get_home_hogwards(self) -> str:
        """
        :return: Возвращает дом Хогвардса
        """
        return self.__home_hogwards

    def get_mana(self):
        """
        :return: Возвращает количество маны
        """
        return self.__mana

    def get_list_spells(self) -> str:
        """
        :return: Возвращает изученных заклинаний
        """
        result = [str(i) for i in self.__list_spells]
        return '\n'.join(result)

    def set_name(self, data: str) -> None:
        """
        Назначает новое название
        :param data: Пренимает новове название
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')

        self.__name = data

    def set_home_hogwards(self, data: str) -> None:
        """
        Назначает новый дом
        :param data: Пренимает новый дом
        :return: None
        """
        if not isinstance(data, str):
            raise TypeError('Получен не верный тип данных, ожидалась строка')

        self.__home_hogwards = data

    def set_mana(self, data: int) -> None:
        """
        Назначает новое значение манны
        :param data: Пренимает новое значение манны
        :return: None
        """
        if not isinstance(data, int):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')

        self.__home_hogwards = data

    def learn_spell(self, data: Spell) -> None:
        """
        Добавляет заклинание в список изученных
        :param data: Пренимает новое заклинание
        :return: None
        """
        if not isinstance(data, Spell):
            raise TypeError('Получен не верный тип данных, ожидались данные типа Spell')

        if data not in self.__list_spells:
            self.__list_spells.append(data)
        else:
            raise ValueError('Заклинание уже изучено')

    def cast_spell(self, target: HogwartsStudent) -> None:
        """
        Рандомно выбирает заклинание из списка изученных и применяет его к цели,
        вычитая стоимость заклинания из маны. Если маны недостаточно, студент пропускает ход.
        :param target: Пренимает цель
        :return: None
        """
        if not isinstance(target, HogwartsStudent):
            raise TypeError('Получен не верный тип данных, ожидались данные типа HogwartsStudent')

        if not len(self.__list_spells) != 0:
            raise ValueError('В списке изученных отсутствуют заклинания, сначала добавьте их')

        if not self.__mana != 0:
            raise ValueError('Количество маны на исходе')

        spell = random.choice(self.__list_spells)
        spell.cast(target)
        self.__mana -= Spell.get_mana_cost(spell)
        if self.__mana == 0:
            return

    def __str__(self):
        return (f'Студент: {self.get_name()}\n'
                f'Дом хогвартса: {self.get_home_hogwards()}\n'
                f'Количество маны: {self.get_mana()}\n'
                f'Список изученных заклинаний: \n{self.get_list_spells()}')

class Spell:

    __name_spell: str
    __description_spell: str
    __mana_cost: int

    def __init__(self, name_spell: str, description_spell: str, mana_cost: int):
        """
        Формирует шаблон объекта Spell
        :param name_spell: Пренимает название заклинания
        :param description_spell: Пренимает описание заклинания
        :param mana_cost: Пренимает количество ,затрачиваемой на использование заклинания, маны
        """
        self.__name_spell = name_spell
        self.__description_spell = description_spell
        self.__mana_cost = mana_cost

    def get_name_spell(self) -> str:
        """
        :return: Возвращает название заклинания
        """
        return self.__name_spell

    def get_description_spell(self) -> str:
        """
        :return: Возвращает описание заклинания
        """
        return self.__description_spell

    def get_mana_cost(self) -> int:
        """
        :return: Возвращает количество ,затрачиваемой на использование заклинания, маны
        """
        return self.__mana_cost

    def set_name_spell(self, data: Spell) -> None:
        """
        Назначет название заклинания
        :return: None
        """
        if not isinstance(data, Spell):
            raise TypeError('Получен не верный тип данных, ожидались данные типа Spell')

        self.__name_spell = data

    def set_description_spell(self, data: Spell) -> None:
        """
        Назначет описание заклинания
        :return: None
        """
        if not isinstance(data, Spell):
            raise TypeError('Получен не верный тип данных, ожидались данные типа Spell')

        self.__description_spell = data

    def set_mana_cost(self, data: int) -> None:
        """
        Назначет количество маны, требуемое для использование заклинания
        :return: None
        """
        if not isinstance(data, Spell):
            raise TypeError('Получен не верный тип данных, ожидалось целое число')

        self.__mana_cost = data

    def cast(self, target: HogwartsStudent) -> None:
        """
        Использует заклинание по отношению к цели
        :param target: Пренимает цель
        :return: None
        """
        print(f'\nСтудент колдует {self.__name_spell} в {target}')

    def __str__(self) -> str:
        return (f'Название заклинания: {self.get_name_spell()}\n'
                f'Описание заклинания: {self.get_description_spell()}\n'
                f'Расход маны: {self.get_mana_cost()}\n')

class Hogwarts:

    __list_students_in_hogwards: list[HogwartsStudent ]
    __list_of_available_spells: list[Spell]

    def __init__(self, list_students_in_hogwards: list[HogwartsStudent] = None, list_of_available_spells: list[Spell] = None):
        """
        Формирует шаблон объекта Hogwarts
        :param list_students_in_hogwards: Пренимает список студентов
        :param list_of_available_spells: Пренимает список заклинаний, доступных для изучения
        """
        if list_students_in_hogwards is None:
            self.__list_students_in_hogwards = []
        else:
            self.__list_students_in_hogwards = list_students_in_hogwards

        if list_of_available_spells is None:
            self.__list_of_available_spells = []
        else:
            self.__list_of_available_spells = list_of_available_spells

    def get_list_students_in_hogwards(self) -> str:
        """
        :return: Возвращает список студентов
        """
        result = [str(i) for i in self.__list_students_in_hogwards]
        return '\n'.join(result)

    def get_list_of_available_spells(self) -> str:
        """
        :return: Возвращает список доступных заклинаний
        """
        result = [str(i) for i in self.__list_of_available_spells]
        return '\n'.join(result)

    def enroll_student(self, data: HogwartsStudent) -> None:
        """
        Добавляет студента в Хогвартс
        :param data: Пренимает студента
        :return: None
        """
        if not isinstance(data, HogwartsStudent):
            raise TypeError('Получен не верный тип данных, ожидались данные типа HogwartsStudent')

        if data in self.__list_students_in_hogwards:
            raise ValueError('Студент уже присутствует в списке, добавьте другого')

        self.__list_students_in_hogwards.append(data)

    def teach_spell(self, data: Spell):
        """
        Добавляет заклинание в список доступных для изучения
        :param data: Пренимает заклинание
        :return:
        """
        if not isinstance(data, Spell):
            raise TypeError('Получен не верный тип данных, ожидались данные типа Spell')

        if data in self.__list_of_available_spells:
            raise ValueError('Данное заклинание уже присутствует в списке для изучения, добавьте другое')

        self.__list_of_available_spells.append(data)

    def simulate_duel(self, valera: HogwartsStudent, jora: HogwartsStudent):
        """
        Организует цикл битвы между двумя студентами
        :param valera: Пренимает студента 1
        :param jora: Пренимает студента 2
        :return: Возвращает результат битвы в виде строки
        """
        while True:
            valera.cast_spell(jora)
            if valera.get_mana() == 0 or valera.get_mana() < 0:
                return f'\nПобедил {jora}'
            jora.cast_spell(valera)
            if jora.get_mana() == 0 or jora.get_mana() < 0:
                return f'\nПобедил {valera}'

    def __str__(self):
        return (f'Студенты Хогвартса: {self.get_list_students_in_hogwards()}\n'
                f'Список доступных заклинаний: {self.get_list_of_available_spells()}\n')

class Progeam:

    @staticmethod
    def main():

        expelliarmus = Spell('Expelliarmus', ' Дизармирование противника, низкая стоимость магической энергии', 5)

        stupefy = Spell('Stupefy', ' Оглушение противника, средняя стоимость магической энергии', 10)

        avada_kedavra = Spell('Avada Kedavra', ' Смертельное ранение (используется редко), высокая стоимость магической энергии', 20)

        protego = Spell('Protego', 'Защитный щит, отражающий заклинания, низкая стоимость магической энергии', 5)

        petrificus_totalus = Spell('Petrificus Totalus', 'Полная парализация противника, средняя стоимость магической энергии', 10)

        lumos = Spell('Lumos', 'Создание источника света на конце волшебной палочки, низкая стоимость магической энергии', 5)

        expecto_patronum = Spell('Expecto Patronum', 'Призывание патронуса для защиты от дементоров, высокая стоимость магической энергии', 20)

        valera = HogwartsStudent('Valera', 'Когтевран')
        valera.learn_spell(protego)
        valera.learn_spell(petrificus_totalus)
        valera.learn_spell(lumos)
        valera.learn_spell(expecto_patronum)

        jora = HogwartsStudent('Jora', ' Гриффиндор')
        jora.learn_spell(expelliarmus)
        jora.learn_spell(stupefy)
        jora.learn_spell(avada_kedavra)

        hogwarts = Hogwarts()
        hogwarts.enroll_student(valera)
        hogwarts.enroll_student(jora)
        hogwarts.teach_spell(expelliarmus)
        hogwarts.teach_spell(stupefy)
        hogwarts.teach_spell(avada_kedavra)
        hogwarts.teach_spell(protego)
        hogwarts.teach_spell(petrificus_totalus)
        hogwarts.teach_spell(lumos)
        hogwarts.teach_spell(expecto_patronum)

        print(hogwarts.simulate_duel(valera, jora))

Progeam.main()