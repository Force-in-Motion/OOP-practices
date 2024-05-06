
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
