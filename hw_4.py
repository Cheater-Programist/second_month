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
    def __init__(self, name, email, phone, student_id):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.group_where_study = []

    def __str__(self):
        return f"{g}, Id: {self.student_id}"

    def study(self, group):
        self.group_where_study.append(group)
        print(f"Studies in {self.group_where_study}")

s = Student("Asd", "asd@gmail.com", "0987655433", 3)
print(s)
s.study("Math")

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id):
        super().__init__(name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = []

    def __str__(self):
        return f"{g}, Id: {self.teacher_id}"

    def teach(self, group):
        self.group_where_teach.append(group)
        print(f"Teaches {self.group_where_teach}")

t = Teacher("Asd", "asd@gmail.com", "0987655433", 3)
print(t)
t.teach("Eng")

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
    def __init__(self, name, email, phone, student_id, teacher_id):
        Student.__init__(self, name, email, phone, student_id)
        Teacher.__init__(self, name, email, phone, teacher_id)

    def __str__(self):
        return f"{g}, Id: {self.student_id}, Teacher id: {self.teacher_id}"
    
m = Mentor("A", "A@gmail.com", "0552878777", 1, 2)
print(m)