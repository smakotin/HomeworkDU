"""Задача 1. Необходимо реализовать код, показанный в примерах выше. Создать класс Rectangle и класс ToyClass.
Для ToyClass необходимо добавить три атрибута, и метод который устанавливает их."""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_heigth(self):
        return self.height

    def get_area(self):
        return self.width * self.height


rect1 = Rectangle(12, 100)
print(rect1.get_area())
