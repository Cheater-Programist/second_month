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

# 2
