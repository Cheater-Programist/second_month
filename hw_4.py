# 1
class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"
    
g = GeeksPeople("Asd", "asd@gmail.com", "0987655433")
print(g)


class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"Studies in {self.group_where_study}")

s = Student("Asd", "asd@gmail.com", "0987655433", 3, "Math")
print(s)
s.study()


class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id=None, group_where_teach=None):
        super().__init__(name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f"Teaches {self.group_where_teach}")

t = Teacher("Asd", "asd@gmail.com", "0987655433", 3, "Eng")
print(t)
t.teach()


class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        super().__init__(name, email, phone)
        self.admin_id = admin_id

    def create_group(self, groups):
        print(f"Created {groups} group")

a = Admin("Asd", "asd@gmail.com", "0987655433", 3)
print(a)
a.create_group("IT")


class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id=None, group_where_teach=None):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)
    
m = Mentor("A", "A@gmail.com", "0552878777", 1,"Math", 1, "Eng")
print(m)
m.study()
m.teach()



# 2
# class GeeksPeople:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
    
#     def __str__(self):
#         return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

# class Student(GeeksPeople):
#     def __init__(self, name, email, phone, student_id, group_where_study):
#         super().__init__(name, email, phone)
#         self.student_id = student_id
#         self.group_where_study = group_where_study
    
#     def study(self):
#         print(f"{self.name} studies in group {self.group_where_study}")

# class Teacher(GeeksPeople):
#     def __init__(self, name, email, phone, teacher_id=None, group_where_teach=None):
#         super().__init__(name, email, phone)
#         self.teacher_id = teacher_id
#         self.group_where_teach = group_where_teach
    
#     def teach(self):
#         print(f"{self.name} teaches in group {self.group_where_teach}")

# class Admin(GeeksPeople):
#     def __init__(self, name, email, phone, admin_id):
#         super().__init__(name, email, phone)
#         self.admin_id = admin_id
    
#     def group(self):
#         print(f"{self.name} creates a group")

# class Mentor(Student, Teacher):
#     def __init__(self, name, email, phone, student_id, group_where_study, teacher_id=None, group_where_teach=None):
#         Student.__init__(self, name, email, phone, student_id, group_where_study)
#         Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)

# student1 = Student("Omurbek", "Omurbek@gmail.com", "12345678", "12345", "A1")
# student2 = Student("Elaman", "Elaman@gmail.com", "87654321", "54321", "B2")
# teacher1 = Teacher("Nurbolot", "Nurbolot@gmail.com", "98765432", "1001", "A1")
# teacher2 = Teacher("Kurmanbek", "Kuma@gmail.com", "23456789", "1002", "B2")
# admin1 = Admin("Ulan", "Ulan@gmail.com", "11111111", "001")
# admin2 = Admin("Beksultan", "Beksultan@gmail.com", "99999999", "002")

# print(student1)
# student1.study()
# print(student2)
# student2.study()

# print(teacher1)
# teacher1.teach()
# print(teacher2)
# teacher2.teach()

# print(admin1)
# admin1.group()
# print(admin2)
# admin2.group()

# mentor = Mentor("kudbuhon", "Kudbuhon@gmail.com", "44444444", "12345", "A1", "1001", "A1")
# mentor.study()
# mentor.teach()