import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS nurbolot(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INTEGER
)''')

# cursor.execute(f'''INSERT INTO nurbolot(first_name, last_name, age) VALUES("Nurbolot", "Erkinbaew", 18)''')
# connect.commit()
# connect.close()

# while True:
#     first_name = input("Type first name: ")
#     last_name = input("Type last name: ")
#     age = int(input("Type age: "))
#     cursor.execute(f'''INSERT INTO nurbolot(first_name, last_name, age)
#     VALUES("{first_name}", "{last_name}", {age})''')
#     connect.commit()
#     connect.close()

cursor.execute('''SELECT * FROM nurbolot''')
data = cursor.fetchall()

for i in data:
    print(f"ID: {i[0]}\nName: {i[1]}\nLast name: {i[2]}\nAge: {i[3]}")
    print("====================================================================================================================================")