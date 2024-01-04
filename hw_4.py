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

    def __str__(self):
        return f"{g}, Id: {self.student_id}"

    def study(self):
        print(f"In {self.group_where_study}")

s = Student("Asd", "asd@gmail.com", "0987655433", 3, "math")
print(s)
s.study()

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        super().__init__(name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def __str__(self):
        return f"{g}, Id: {self.teacher_id}"

    def teach(self):
        print(f"Teaches {self.group_where_teach}")

t = Teacher("Asd", "asd@gmail.com", "0987655433", 3, "math")
print(t)
t.teach()

class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        super().__init__(name, email, phone)
        self.admin_id = admin_id

    def __str__(self):
        return f"{g}, Id: {self.admin_id}"

    groups = []
    def create_group(self):
        a = input("What group wanna create: ")
        print("Created")
        self.groups.append(a)

a = Admin("Asd", "asd@gmail.com", "0987655433", 3)
print(a)
a.create_group()
print(a.groups)

class Mentor(Student, Teacher):
    pass

    def __str__(self):
        return f"{g}, Id: {self.student_id}, {self.group_where_teach}"
    
# m = Mentor(name=s.name, email=s.email, phone=s.phone, student_id=s.student_id)
print()