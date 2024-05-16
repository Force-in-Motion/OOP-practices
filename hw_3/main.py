
class Potion:

    def __init__(self, name_potion: str, ingredients: [], difficulty_preparation: int, effect: str, state_change: str):
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

    def set_add_ingridients(ingridient):
        """
        Добавляет ингридиент в зелье
        :param ingridient: Пренимает ингидиент
        :return:
        """
        
