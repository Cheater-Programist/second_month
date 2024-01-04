# Магические методы - dunder методы (методы с двойным подчеркиванием)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.addres = None
    
    def info(self):
        print(self.name, self.age, self.addres)

    # Магический метод __str__
    def __str__(self): # print
        return f"{self.name}, {self.age}, {self.addres} это метод str"
    
    def __repr__(self): # print
        return f"{self.name}, {self.age}, {self.addres} это метод repr"
    
    # Магический метод __call__
    def __call__(self, location):
        self.addres = location

    # Магический методы для арифметический действий
    def __add__(self, other): # +
        res = self.age + other.age
        return Person(self.name, res)
    
    def __sub__(self, other): # -
        res = self.age - other.age
        return Person(self.name, res)
    
    def __mul__(self, other): # *
        res = self.age * other.age
        return Person(self.name, res)
    
    def __truediv__(self, other): # /
        res = self.age / other.age
        return Person(self.name, res)

    def __floordiv__(self, other): # //
        res = self.age // other.age
        return Person(self.name, res)
    
    # Магическме методы для операторов сравнения (>, <, ==)

    def __gt__(self, other): # >
        return self.age > other.age
    
    def __lt__(self, other): # <
        return self.age < other.age
    
    def __eq__(self, other): # ==
        return self.age == other.age
    
    def __ne__(self, other): # !=
        return self.age != other.age
    
    def __ge__(self, other): # >=
        return self.age >= other.age
    
    def __le__(self, other): # <=
        return self.age <= other.age

muhammadamin = Person("Muhammadamin", 19) # __init__
elaman = Person("Elaman", 28)
# elaman("г. Ош") # __call__
# print(muhammadamin) # __str__
# print(muhammadamin.name, muhammadamin.age, muhammadamin.addres)
print(elaman)
# muhammadamin.info()
# elaman.info()

# Арифметическме действия
print(muhammadamin + elaman)
print(muhammadamin - elaman)
print(muhammadamin * elaman)
print(muhammadamin / elaman)
print(muhammadamin // elaman)

# Операторы сравнения
print(muhammadamin > elaman)
print(muhammadamin < elaman)
print(muhammadamin == elaman)
print(muhammadamin != elaman)
print(muhammadamin >= elaman)
print(muhammadamin <= elaman)