#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Основы ООП, класс, объект, метод и атрибут
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


john = User("John", "Doe")
# john.first_name = "John"

artur = User("Artur", "Doe")
# artur.first_name = "Artur"

# print(john.first_name, john.last_name)
# print(artur.first_name, artur.last_name)
print(john.full_name())
