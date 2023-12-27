class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


    def login(self):
        print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}")

class Student(User):
    def __init__(self, name, email, password, student_id, courses_enrolled):
        super().__init__(name, email, password)
        self.student_id = student_id
        self.courses_enrolled = courses_enrolled

    def login(self):
        print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Id: {self.student_id}, Enrolled courses: {self.courses_enrolled}")

    def enroll_in_course(self):
        a = input("What course wanna enroll: ")
        self.courses_enrolled = a

class Teacher(User):
    def __init__(self, name, email, password, teacher_id, courses_teaching):
        super().__init__(name, email, password)
        self.teacher_id = teacher_id
        self.courses_teaching = courses_teaching
    
    def login(self):
        print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Id: {self.teacher_id}, Teaching courses: {self.courses_teaching}")

    def assign_grade(self):
        a = int(input(f"What mark wanna put: "))
        print(f"You put {a}")

class Admin(User):
    def __init__(self, name, email, password, admin_id):
        super().__init__(name, email, password)
        self.admin_id = admin_id
    
    def login(self):
        print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Id: {self.admin_id}")


    def create_course(self):
        a = input("What course wanna to create: ")
        print(f"You created {a} course")

class TeachingAssistant(Student, Teacher):
    pass
    def __init__(self, name, email, password, student_id, courses_teaching, teacher_id):
        Student.__init__(name, email, password, student_id)
        Teacher.__init__(name, email, password, teacher_id, courses_teaching)

    def login(self):
        print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Id: {self.student_id}, Enrolled courses: {self.courses_enrolled}, Teaching courses: {self.courses_teaching}")



user = User("hello", "hello@gmail.com", "hello1234")
user.login()

stud = Student("hello", "hello@gmail.com", "hello1234", 2, "LL")
stud.login()

teach = Teacher("hello", "hello@gmail.com", "hello1234", 2, "Eng")
teach.login()

admin = Admin("hello", "hello@gmail.com", "hello1234", 2)
admin.login()

studteach = TeachingAssistant("hello", "hello@gmail.com", "hello1234", 2, teacher_id=2, courses_teaching="LL")
studteach.login()