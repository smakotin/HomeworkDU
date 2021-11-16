"""Задача 2. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge,
getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента,
метод getAge нужен для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения
данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов
установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы."""


class Student:
    def __init__(self, name='Ivan', groupNumber='10A', age=18):
        self.__name = name
        self.__groupNumber = groupNumber
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGroupNumber(self):
        return self.__groupNumber

    def setNameAge(self, name, age):
        self.__name = name
        self.__age = age

    def setGroupNumber(self, groupNumber):
        self.__groupNumber = groupNumber


student1 = Student()

print(student1.getAge())
print(student1.getGroupNumber())
print(student1.getName())

student1.setNameAge('Pavel', 109)

print(student1.getAge())
print(student1.getGroupNumber())
print(student1.getName())

student2 = Student('Petr', '31a', 19)
student3 = Student('Sergey', '12d', 20)
student4 = Student('Alexander', '33o', 21)
student5 = Student('Anna', '11k', 22)
