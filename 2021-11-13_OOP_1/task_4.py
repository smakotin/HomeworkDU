"""Задача 4. Напишите программу с классом Car. Создайте конструктор класса Car.
Создайте атрибуты класса Car — color (цвет), type (тип), year (год). Напишите пять методов.
Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
Пятый — присвоение автомобилю цвета."""


class Car:

    def __init__(self, color, type_auto, year, is_started=False):
        self.__color = color
        self.__type_auto = type_auto
        self.__year = year
        self.__is_started = is_started

    def start(self):
        if not self.__is_started:
            self.__is_started = True
            return 'the car is running'
        else:
            return 'the car is already running'

    def shutdown(self):
        if self.__is_started:
            self.__is_started = False
            return 'the car is stopped'
        else:
            return 'the car is already stopped'

    def set_year(self, year):
        self.__year = year

    def set_type_auto(self, type_auto):
        self.__type_auto = type_auto

    def set_color(self, color):
        self.__color = color


car1 = Car('green', 'heavy', 1255)
print(car1.shutdown())
