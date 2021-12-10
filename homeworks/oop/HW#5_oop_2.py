#1 Make the class with composition.

import dataclasses
from collections import namedtuple

class Laptop:
    def __init__(self,):
        battery_1 = Battery("This is battery 1")
        battery_2 = Battery("This is battery 2")
        self.batteries = (battery_1, battery_2)

class Battery:
    def __init__(self, mAh):
        self.mAh = mAh

laptop = Laptop()

print(laptop.batteries[0].mAh)
print(laptop.batteries[1].mAh)

#2 Make the class with aggregation

class Guitar:
    def __init__(self, number_of_strings):
        self.number_of_strings = number_of_strings

class GuitarString:
    def __init__(self):
        pass

guitarstring = GuitarString()
guitar = Guitar(guitarstring)

#3 Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
# Note: this method should be static

class Calc:

    @staticmethod
    def add_nums(x ,y, z):
        return x + y + z

print(Calc.add_nums(5, 6, 7))

#4 Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
# It should have 2 methods:
# carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
# which should create Pasta instances with predefined list of ingredients.

class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pasta({self.ingredients!r})'

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


carbonara_pasta = Pasta.carbonara()
bolognaise_pasta = Pasta.bolognaise()
print(carbonara_pasta)
print(bolognaise_pasta)

# 5 Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """

class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= self.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num

Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

# 6 class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

#7 Create the same class (6) but using NamedTuple

AddressBookDataClass1 = namedtuple("AddressBookDataClass", ["key", "name", "phone_number", "address", "email", "birthday", "age"])

person_2 = AddressBookDataClass1(2, "Mukola", "123456789", "Kiev", "ex@2.com", "02.02.2002", 19)

print(person_2)

#8 class AddressBook:
    # """
    # Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    # Make its str() representation the same as for AddressBookDataClass defined above.
    # Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
    # """

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.mail = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'addresbook {self.key}, {self.name}, {self.phone_number}, {self.address}, ' \
            f' {self.mail}, {self.birthday}, {self.age} '

person_3 = AddressBook(3, "Sergio", "555", "Odessa", "ex@3.com", "03.03.2003", 18)

print(person_3)

#9 Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def what_the_age(self):
        return f'This person name is {self.name}, and he is {self.age} old and live in country {self.country}'

person_4 = Person('John', 36, 'USA')
print(person_4.what_the_age)
person_4.age = 20
print(person_4.what_the_age)

#10 Add an 'email' attribute of the object student and set its value
    # Assign the new attribute to 'student_email' variable and print it by using getattr
    # """
    # id = 0
    # name = ""
    #
    # def __init__(self, id, name):
    #     self.id = id
    #     self.name = name

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(id = 0, name = 'Ivan')

setattr(Student, 'email', 'ex@4.com')

print(getattr(student, 'email'))

#11 By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     """
#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, add_temp):
        self._temperature = add_temp


fahrenheit = Celsius(-3)
fahrenheit.temperature = (fahrenheit.temperature * 1.8) + 32
print(fahrenheit.temperature)