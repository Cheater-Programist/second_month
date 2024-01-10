# import sqlite3
# import random

# connect = sqlite3.connect("user_random.db")
# cursor = connect.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS customers(
#                name VARCHAR(255),
#                surname VARCHAR(255),
#                age INTEGER,
#                email VARCHAR(255),
#                password VARCHAR(255)
# )''')

# class Game:
#     def game(self):
#         n = 0
#         limit = 5
#         while True:
#             randon = random.randint(1,5)
#             user = int(input("Type a number 1-5: "))
#             if limit != 0:
#                 if n != 5:
#                     pass
#                 else:
#                     print("you win")
#                     break
#             else:
#                 print("you lose")
#                 break 
#     def registration(self, name, surname, age, email, password, con_password):
#         if age >= 18:
#             if len(password) >= 8:
#                 if "123" not in password:
#                     if password == con_password:
#                         cursor.execute('''INSERT INFO customers(name, surname, age, email, password) VALUES("{name}", "{surname}", {age}, "{email}", "{password}")''')
#                         connect.commit()
#                         print("")
#                         print(f"Dear {name} {surname}, you signed up")
#                     else:
#                         print(f"Dear {name} {surname}, your passwords aren't eaquls")
#                 else:
#                     print(f"Dear {name} {surname}, your password is too easy")
#             else:
#                 print(f"Dear {name} {surname}, your password is too short")
#         else:
#             print(f"Dear {name} {surname}, your age is less than 18")



# sent
class Dad:
    def dad_info(self):
        return "Это от деда"
class Father(Dad):
    def father_info(self):
        return "Это от отца"
class Son(Father):
    def son_info(self):
        return "Это от сына!"
    
# dad = Dad()
# print(dad.dad_info())
    
# father = Father()
# print(father.father_info())
# print(father.dad_info())
    
# son = Son()
# print(son.son_info())
# print(son.dad_info())
# print(son.father_info())


import sqlite3
import   random
connect  = sqlite3.connect("users_random.db")
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS clients(
            name VARCHAR(255),
            surname VARCHAR(255),
            age INTEGER,
            email VARCHAR(255),
            password VARCHAR(255)
)''')
class Game:
    def game(self):
        n = 0 
        limit = 5
        while True:
            randon = random.randint(1,5)
            user = int(input("Введите число: "))

            if limit != 1:
                if n !=5:
                    if user ==randon:
                        n +=1
                        print(f"Вы угадали, Бот выбрал: {randon}. Выигрыш: {n}. Количество попыток: {limit}")
                    else:
                        limit-=1
                        print(f"Вы не угадали, Бот выбрал: {randon}. Выигрыш: {n}. Количество попыток: {limit}")

                else:
                    print(f"Вы выиграли, у вас 5 баллов!!! Выигрыш: {n}. Количество попыток: {limit}")
                    break
            else:
                print(f"Вы проиграли, у вас закончились попытки!!! Выигрыш: {n}. Количество попыток: {limit}")
                break


    def register(self,name,surname,age,email,password,confirm_password):
        if password ==confirm_password:
            cursor.execute(f'''INSERT INTO clients(name,surname,age,email,password) VALUES('{name}','{surname}',{age},'{email}','{password}')''')
            connect.commit()
            print("")
            print(f"Уважаемый {name} {surname},Вы успешно прошли регистрацию")
            print("")
            self.game()
        else:
            print(f"Уважаемый {name} {surname}, вы не прошли регистрацию. Пароли не совпадают !!")
                

    def main(self):
        name = input("Введиие имя: ")
        surname = input("Введите фамилию: ")
        age = int(input("Введите возраст: "))
        email = input("Введите почту: ")
        password = input("Введите пароль: ")
        confirm_password = input("Потвердите пароль: ")
        if age >=18:
            if len(password) >=8:
                if "123" not in password:
                    self.register(name,surname,age,email,password,confirm_password)
                else:
                    print(f"Уважаемый {name} {surname}, вы не прошли регистрацию. Пароль простой!!")
            else:
                print(f"Уважаемый {name} {surname}, вы не прошли регистрацию. Пароль короткий!!")
        else:
            print(f"Уважаемый {name} {surname}, вы не прошли регистрацию. Вам нет 18лет!!")

game_user = Game()
game_user.main()