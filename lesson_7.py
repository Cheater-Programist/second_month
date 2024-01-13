import sqlite3

conn = sqlite3.connect("bank.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY,
            name VARCHAR(255),
            surname VARCHAR(255),
            age INTEGER,
            bio TEXT,
            balance INTEGER,
            wallet_id VARCHAR(16),
            email VARCHAR(255)
)""")

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.bio = None
        self.balance = 0
        self.wallet_id = None
        self.email = None

    def registration(self, name, surname, age, email, bio):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.bio = bio

        cur.execute(f'''INSERT INTO clients(name, surname, age, bio, balance, wallet_id, email) VALUES("{self.name}", "{self.surname}", {self.age}, "{self.bio}", {self.balance}, "1234123412341234", "{self.email}")''')
        conn.commit()

    def info(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nWallet id: {self.wallet_id}\nBalance: {self.balance}\nEmail: {self.email}\nBIO: {self.bio}"

    def deposit(self, amount):
        cur.execute(f"UPDATE clients SET balance = balance + {amount} WHERE email = '{self.email}'")
        conn.commit()
        self.balance += amount
        print(f"\nDear {self.name} {self.surname}, congratulations, you cashed in\n")

    def cash_out(self, amount):
        if amount <= self.balance:
            cur.execute(f"UPDATE clients SET balance = balance - {amount} WHERE email = '{self.email}'")
            conn.commit()
            self.balance -= amount
            print(f"\nDear {self.name} {self.surname}, here you are, you cashed out\n")
        else:
            print("You don't anough money")


    def main(self):
        while True:
            commands = input("1 - registration, 2 - info, 3 - cash in, 4 - cash out, 5 - exit: ")

            if commands == "1":
                print("====================================================================================================================================")
                name = input("Type name: ")
                surname = input("Type surname: ")
                age = int(input("Type age: "))
                email = input("Type email(example@gmail.com): ")
                bio = input("Type bio: ")
                print("====================================================================================================================================")

                if "@gmail.com" in email:
                    if age >= 16:
                        self.registration(name, surname, age, email, bio)
                        print(f"\nDear {name} {surname}, congratulations, you logged up\n")
                    else:
                        continue
                else:
                    continue
            
            elif commands == '2':
                print(self.info())

            elif commands == "3":
                self.deposit(int(input("Type amount: ")))
            
            elif commands == '4':
                print(f"You have: {self.balance}")
                self.cash_out(int(input("Type how much: ")))

            elif commands == '5':
                break

bank = Bank()
bank.main()