# class Animal:
#     name = "Cow"  #Атрибут
    
#     def make_sound(self, sound):  #Метод
#         print(f"{self.name} sounds '{sound}'")

# animal = Animal()
# animal.make_sound("Muuuu")


# class Calculator:
    
#     def add(self, num1, num2):
#         print(f'Result: {num1 + num2}')

#     def minus(self, num1, num2):
#         print(f"Result: {num1 - num2}")

#     def multiply(self, num1, num2):
#         print(f"Result: {num1 * num2}")

#     def devide(self, num1, num2):
#         print(f"Result: {int(num1 / num2)}")
        
# calc = Calculator()  #Эгземпляр класса
# calc.add(32, 12)
# calc.minus(32, 12)
# calc.multiply(32, 12)
# calc.devide(32, 12)


# class Book:

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
        
#     def info(self):
#         print(f"Book: {self.title}, Author: {self.author}")

# book = Book("Harry Poter", "Geeks")
# book.info()

# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
    
#     def result(self):
#         print(f"Mark: {self.model}, Year: {self.year}")
    
# car = Car(input("What's model: "), int(input("What's year: ")))
# car.result()