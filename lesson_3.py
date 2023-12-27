# class Transport: # Абстрактный класс, Родительский класс
#     def __init__(self, model, year, color):
#         self.model = model # Публичный атрибут
#         self._year = year # Защищенный атрибут
#         self.__color = color # Приватный атрибут

#     @property
#     def color(self):
#         return self.__color
    
#     def __secret_info(self):
#         print("Не законные документы")
    
#     @property
#     def secret_info(self):
#         return self.__secret_info

#     def _drive(self): # Защищенный метод
#         print("Машина едет со скоростью 200 км/ч")
    
#     def info(self): # Публичный метод
#         print(f"model: {self.model}, year: {self._year}, color: {self.color}")
#         self._drive()
#         self.__secret_info()




# car = Transport("tesla", 2021, "White")
# print(car)
# print(car.model) # Публичный атрибут
# print(car.year) # Защищенный атрибут
# print(car.color) # Приватный атрибут
# car.info()
# car.drive()
# car.secret_info()

# class Car(Transport):
#     def __init__(self, model, year, color, penalties = 0):
#         # Transport.__init__(self, model, year, color)
#         super().__init__(model, year, color)
#         self.penalties = penalties

#     def info(self):
#         print(f"model: {self.model}, year: {self.year}, color: {self.color}, penalties: {self.penalties}")
    
# tesla = Car("tesla Model X", 2019, "Black", 2000)
# tesla.info()

# class Animal:
#     def __init__(self):
#         pass
#         # self.name = name
#         # self.breed = breed
#         # self.age = age

#     def speak(self):
#         pass

# class Dog(Animal):
#     pass

#     def speak(self):
#         print("Gaf-Gaf")

# class Cat(Animal):
#     pass

#     def speak(self):
#         print("Meow")

# class Cow(Animal):
#     pass

#     def speak(self):
#         print("Muuu")


# def speak():
#     print("Gaf")
# speak()

# def speak():
#     print("Meow")
# speak()

# def speak():
#     print("Muu")

# speak()

# bobik = Dog()
# bobik.speak()

# pofig = Cat()
# pofig.speak()

# murka = Cow()
# murka.speak()

# Декораторы

# def decorator(a):
#     def change():
#         print("Hello world!")
#         a()
#         print("Goodbye!")
#     return change

# @decorator
# def hi():
#     print("Hi!")
# hi()

