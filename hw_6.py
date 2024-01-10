import sqlite3

connect = sqlite3.connect("library.db")
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY,
            title VARCHAR(255),
            author VARCHAR(255),
            year INTEGER
)''')
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def d_base(self):
        cursor.execute(f'''INSERT INTO books(title, author, year) VALUES("{self.title}", "{self.author}", {self.year})''')
        connect.commit()

    def display_info(self):
        print(f"Book: {self.title}, Author: {self.author}, Year: {self.year}")
    
    def create(self):
        self.title = input("Type title: ")
        self.author = input("Type the author: ")
        self.year = int(input("Type year: "))
        cursor.execute(f'''INSERT INTO books(title, author, year) VALUES("{self.title}", "{self.author}", {self.year})''')
        connect.commit()
        # connect.close()

    def update(self):
        cursor.execute('''SELECT * FROM books''')
        data = cursor.fetchall()

        for i in data:
            print(f"ID: {i[0]}, Title: {i[1]}, Author: {i[2]}, Year: {i[3]}")
            print("====================================================================================================================================")

        a = int(input("Which one wanna change(ID): "))
        for i in data:
            if i[0] == a:
                print(f"Author: {i[2]}, Year: {i[3]}")
                print("====================================================================================================================================")
                print("1 - Author, 2 - Year")
                b = int(input("What wanna change: "))
                if b == 1:
                    cursor.execute(f'''UPDATE books SET author = "{input("Type author: ")}" WHERE id = {a}''')
                    # i[2] = input("Type author: ")
                    # print(i)
                elif b == 2:
                    cursor.execute(f'''UPDATE books SET year = {int(input("Type year: "))} WHERE id = {a}''')
                    # i[3] = int(input("Type year: "))
                else:
                    print("Type correctly!")
    
    def delete(self):
        cursor.execute('''SELECT * FROM books''')
        data = cursor.fetchall()

        for i in data:
            print(f"ID: {i[0]}, Title: {i[1]}, Author: {i[2]}, Year: {i[3]}")
            print("====================================================================================================================================")

        a = input("Which one wanna delete(title): ")
        for i in data:
            if i[1] == a:
                # print(f"Author: {i[2]}, Year: {i[3]}")
                # print("====================================================================================================================================")
                cursor.execute(f'''DELETE FROM books WHERE "{i[1]}" = "{a}"''')




book1 = Book("Book1", "Author1", 2020)
book1.d_base()
book1.create()
book1.create()

book1.display_info()

book1.update()

book1.delete()
book1.display_info()