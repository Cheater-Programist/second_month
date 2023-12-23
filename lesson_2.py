# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info_user(self):
#         print(f"Hello! My name is {self.name} and i'm {self.age}")
    
# person = Person("Nurbolot", 19)
# person.info_user()

# class Father:
#     def car(self):
#         print("I have a car")

# father = Father()
# father.car()

# class Son(Father):
#     pass

# son = Son()
# son.car()

# class Father:
#     def info_father(self):
#         print("I'm a father")

# class Mother:
#     def info_mother(self):
#         print("I'm a mother")

# class Son(Father, Mother):
#     def info_son(self):
#         print("I'm a son")

# son = Son()
# son.info_father()
# son.info_mother()
# son.info_son()


# class Phone:
#     def call(self):
#         print("I'm calling mum")
    
# class Camera:
#     def take_photo(self):
#         print("I'm taking a photo for my father")
    
# class Smartphone(Phone, Camera):
#     def alll(self):
#         print("I'm taking a photo and calling")

# smartphone = Smartphone()
# smartphone.call()
# smartphone.take_photo()
# smartphone.alll()


# class Animals:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animals):
#     def sound(self):
#         return "Guf guf guf"
    
# dog = Dog("Dog")
# print(f"{dog.name}: {dog.sound()}")


# class User:
#     def __init__(self, name, lastname, age, phone, email):
#         self._name = name            #Защищенный
#         self.__lastname = lastname   #Приватный
#         self.age = age               #Публичный
#         self.phone = phone
#         self.email = email
#     def info(self):
#         print(f"""Name: {self.name}
# lastname: {self.lastname}
# age: {self.age}
# number: {self.phone}
# email: {self.email}""")

# user = User("Nur", "Nurov", 15, "+994445566", "nur@gmail.com")
# user.info()

