#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Основы ООП - конструктор, наследование, перегрузка, полиморфизм, инкапсуляция
#


class User:
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        # return self.first_name + self.last_name
        return f"Fullname: {self.first_name} {self.last_name}"

    def show_age(self):
        print("I have no age")


class AgedUser(User):
    __age: int

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name)
        self.__age = age

    def full_name(self):
        return super().full_name() + f", Age: {self.__age}"

    def show_age(self):
        print(self.__age)


unaged_artur = User("Artur", "Doe")
unaged_artur.show_age()

aged_john = AgedUser("John", "Doe", 42)
# aged_john.__age = 32
# print(aged_john.full_name())

aged_john.show_age()
