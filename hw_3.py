# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     def login(self):
#         print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}")

# class Student(User):
#     def __init__(self, name, email, password, student_id, courses_enrolled):
#         super().__init__(name, email, password)
#         self.student_id = student_id
#         self.courses_enrolled = courses_enrolled

#     def login(self):
#         print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Id: {self.student_id}, Enrolled courses: {self.courses_enrolled}")

#     def enroll_in_course(self):
#         a = input("What course wanna enroll: ")
#         self.courses_enrolled = a

# class Teacher(User):
#     def __init__(self, name, email, password, teacher_id, courses_teaching):
#         super().__init__(name, email, password)
#         self.teacher_id = teacher_id
#         self.courses_teaching = courses_teaching
    
#     def login(self):
#         print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Id: {self.teacher_id}, Teaching courses: {self.courses_teaching}")

#     def assign_grade(self):
#         a = int(input(f"What mark wanna put: "))
#         print(f"You put {a}")

# class Admin(User):
#     def __init__(self, name, email, password, admin_id):
#         super().__init__(name, email, password)
#         self.admin_id = admin_id
    
#     def login(self):
#         print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Id: {self.admin_id}")


#     def create_course(self):
#         a = input("What course wanna to create: ")
#         print(f"You created {a} course")

# class TeachingAssistant(Student, Teacher):
#     pass
#     def __init__(self, name, email, password, student_id, courses_teaching, teacher_id):
#         Student.__init__(name, email, password, student_id)
#         Teacher.__init__(name, email, password, teacher_id, courses_teaching)

#     def login(self):
#         print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Id: {self.student_id}, Enrolled courses: {self.courses_enrolled}, Teaching courses: {self.courses_teaching}")



# user = User("hello", "hello@gmail.com", "hello1234")
# user.login()

# stud = Student("hello", "hello@gmail.com", "hello1234", 2, "LL")
# stud.login()

# teach = Teacher("hello", "hello@gmail.com", "hello1234", 2, "Eng")
# teach.login()

# admin = Admin("hello", "hello@gmail.com", "hello1234", 2)
# admin.login()

# studteach = TeachingAssistant("hello", "hello@gmail.com", "hello1234", 2, teacher_id=2, courses_teaching="LL")
# studteach.login()


# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     def login(self):
#         return f"User {self.name} logged in."

# class Student(User):
#     def __init__(self, name, email, password, student_id):
#         super().__init__(name, email, password)
#         self.student_id = student_id
#         self.courses_enrolled = []

#     def enroll_in_course(self, course):
#         self.courses_enrolled.append(course)
#         return f"Student {self.name} enrolled in course {course}."

# class Teacher(User):
#     def __init__(self, name, email, password, teacher_id):
#         super().__init__(name, email, password)
#         self.teacher_id = teacher_id
#         self.courses_teaching = {}

#     def assign_grade(self, student, course, grade):
#         if course in self.courses_teaching:
#             self.courses_teaching[course][student] = grade
#             return f"Teacher {self.name} assigned grade {grade} to {student} in course {course}."
#         else:
#             return f"Teacher {self.name} is not teaching course {course}."

# class Admin(User):
#     def __init__(self, name, email, password, admin_id):
#         super().__init__(name, email, password)
#         self.admin_id = admin_id

#     def create_course(self, course):
#         return f"Admin {self.name} created course {course}."

# class TeachingAssistant(Student, Teacher):
#     def __init__(self, name, email, password, student_id, teacher_id):
#         Student.__init__(self, name, email, password, student_id)
#         Teacher.__init__(self, name, email, password, teacher_id)

# # Example usage
# student1 = Student("Alice", "alice@email.com", "pass123", "S001")
# teacher1 = Teacher("Professor Smith", "professor@email.com", "pass456", "T001")
# admin1 = Admin("Admin1", "admin@email.com", "adminpass", "A001")
# ta1 = TeachingAssistant("Bob", "bob@email.com", "pass789", "S002","T002")

# print(student1.login())
# print(student1.enroll_in_course("Math101"))

# print(teacher1.login())
# print(teacher1.assign_grade("S001", "Math101", "A"))

# print(admin1.login())
# print(admin1.create_course("Physics202"))

# print(ta1.login())
# print(ta1.enroll_in_course("Chemistry101"))
# print(ta1.assign_grade("S002", "Chemistry101", "B"))


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


    def login(self):
        print(f"Name: {self.name}, Email: {self.email}, Password: {self.password}")

user = User("Max", "Max@gmail.com", "123")
user.login()

class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id
        self.courses_enrolled = []

    def enroll_in_course(self, course):
        self.courses_enrolled.append(course)
        print(f"{self.name} studies in {course} course.")

student1 = Student("Nurbolot", "Nurbolot@gmail.com", "02123", "S001")
student1.login()
student1.enroll_in_course("Math")


class Teacher(User):
    def __init__(self, name, email, password, teacher_id):
        User.__init__(self, name, email, password)
        self.teacher_id = teacher_id
        self.courses_teaching = []

teacher = Teacher("Askat", "Askat@gmail.com", "01123", 1)
teacher.login()


class Admin(User):
    def __init__(self, name, email, password, admin_id):
        super().__init__(name, email, password)
        self.admin_id = admin_id


    def create_course(self, course):
        print(f"Course {course} created.")

class TeachingAssistant(Student):
    def __init__(self, name, email, password, student_id, teacher_id):
            Student.__init__(self, name, email, password, student_id)
            Teacher.__init__(self, name, email, password, teacher_id)


    def assist_course(self, course):
        print(f"{self.name} is assisting {course}")


student1 = Student("Nurbolot", "Nurbolot@gmail.com", "02123", "S001")
student1.login()
student1.enroll_in_course("Backend")

admin1 = Admin("Admin", "admin@gmail.com", "admin123", "A001")
admin1.login()
admin1.create_course("Physics")

ta1 = TeachingAssistant("Alex", "alex@gmail.com", "alex123", "S002", "T002")
ta1.login()
ta1.enroll_in_course("Computer Science")
ta1.assist_course("Physics")