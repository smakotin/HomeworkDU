"""Задача 3. Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы:
addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание.
При передаче в методы параметров a и b с ними нужно производить соответствующие действия
и печатать ответ."""


class Math:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b

    @staticmethod
    def subtraction(a, b):
        return a - b

    