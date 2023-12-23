import random

class SlotMachine:
    
    def __init__(self, name):
        self.name = name

    user_balance = 100
    game_balance = 0

    def info(self):
        print(f"Name: {self.name}, Balance: {self.user_balance}, Game balance: {self.game_balance}")
    
    def top_up_balance(self):
        while True:
            a = int(input("How much wanna to put: "))
            if a > 100:
                print("Вы можете пополнить до 100$")
            else:
                self.user_balance -= a
                break
    
    def balance_up(self):
        self.game_balance += 100 - self.user_balance

    def game(self):
        a = 5
        while True:
            a -= 1
            b = random.randrange(1, 10)
            num = int(input('Type a number 1 - 10: '))

            if a == 0:
                print("Вы проиграли")
                self.user_balance -= 10
                break
            elif b != num:
                print(f"Не правильно, у вас еще {a} попыток(а)")
            elif b == num and a > 0:
                print("Вы выиграли")
                self.user_balance += 50
                break
    
    def conslusion_money(self):
        while True:
            a = int(input("How much do you wanna take out: "))

            if a >= 50:
                self.user_balance += a
                self.game_balance -= a
                break
            else:
                print("Вывести можно от 50$")

    def main(self):
        self.info()
        self.top_up_balance()
        self.game()
        self.conslusion_money()

slot = SlotMachine(input("Your name: "))
slot.main()