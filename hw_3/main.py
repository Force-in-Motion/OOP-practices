
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



potion = Potion('Зелье скорости', 10, 'Увеличение скорости бега', True)
print(potion)
potion.set_add_ingridients('Бычьи яйца',)
potion.set_del_ingridients('Гвозди')
potion.set_difficulty(8)
potion.set_create_potion()
potion.set_effect_potion('Уменьшение гравитации')
potion.get_state_potion()
potion.get_info_ingredients()
print(potion)


