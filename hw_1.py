# Задача 1
# class Student:
#     def __init__(self, name, surname, ticket, course : list):
#         self.name = name
#         self.surname = surname
#         self.ticket = ticket
#         self.course = list(course)
        

#     def info(self):
#         print(f"Name: {self.name}, surname: {self.surname}, student ticket: {self.ticket}, course(s): {self.course}")
    
#     def to_add(self):
#         a = input("Add a course: ")
#         self.course.append(a)

#     def to_remove(self):
#         while True:
#             print(self.course)
#             a = input("Which wanna to remove: ")
#             if a in self.course:
#                 self.course.remove(a)
#                 break
#             else:
#                 print("Type correctly")

# stud = Student(input("Type name: "), input("Type surname: "), int(input("Typy ticket: ")), input("Type corse: "))
# stud.to_add()
# stud.to_remove()
# stud.info()


# Задача 2
# class Library:
    
#     def __init__(self, name, author, status = True, books = [{"Name" : "","Aythor" : "","Status" : True}]):
#         self.name = name
#         self.author = author
#         self.status = status
#         self.books = [{"Name" : self.name, "Author" : self.author, "Status" : self.status}]

#     def add(self):
#         new_name = input("Type the name: ")
#         new_author = input("Type the author: ")
        
#         libr = {
#             "Name" : new_name,
#             "Aythor" : new_author,
#             "Status" : True
#         }
#         self.books.append(libr)
#         print(self.books)

#     def delete(self):
#         lst = []
#         for i in self.books:
#             lst.append(i["Name"])
#         print(lst)
#         a = input("Which wanna to remove: ")
#         for i in self.books:
#             if a == i["Name"]:
#                 self.books.remove(i)
#                 print(self.books)

#     def to_give(self):
#         lst = []
#         for i in self.books:
#             lst.append(i["Name"])
#         print(lst)
#         a = input("Which wanna get: ")
#         for i in self.books:
#             if a == i["Name"]:
#                 if i["Status"] == True:
#                     print("Here you are")
#                     i["Status"] = False
#                 else:
#                     print("It's gotten")
#                 print(self.books)

#     def to_return(self):
#         lst = []
#         for i in self.books:
#             if i["Status"] == False:
#                 lst.append(i["Name"])
#         print(lst)
#         a = input("Which wanna return: ")
#         for i in self.books:
#             if a == i["Name"]:
#                 print("Thanks")
#                 i["Status"] = True
#         else:
#             print("Type correctly")
#             print(self.books)


# library = Library("Name", "Author")
# library.add()
# library.add()
# library.add()
# library.delete()
# library.to_give()
# library.to_return()


# Задача 3
# class Shape:
#     pass

#     def s(self):
#         pass

# class Round(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def s(self):
#         print(f"S = {(self.radius * 2) * 3,14}")

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def s(self):
#         print(f"S = {self.side * self.side}")

# class Triangle(Shape):
#     def __init__(self, side, hieght):
#         self.side = side
#         self.hieght = hieght

#     def s(self):
#         print(f"S = {(self.hieght * 2) * self.side}")

# r = Round(5)
# s =Square(5)
# t = Triangle(5, 3)
# r.s()
# s.s()
# t.s()