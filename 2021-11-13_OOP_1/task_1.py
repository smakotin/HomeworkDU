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


class ToyClass:
    def __init__(self, attr1=1, attr2=2, attr3=3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def set_attr(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

toy1 = ToyClass(100, 200, 300)
toy1.set_attr(7, 8, 9)

print(toy1.attr1, toy1.attr2, toy1.attr3)
print(toy1.instancemethod())
print(ToyClass.instancemethod(toy1))
print(ToyClass.classmethod())
print(toy1.classmethod())
print(toy1.staticmethod())
print(ToyClass.staticmethod())
