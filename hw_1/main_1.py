
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
