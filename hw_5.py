import sqlite3

connect = sqlite3.connect('cars.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cars(
    id INTEGER PRIMARY KEY,
    mark VARCHAR(255),
    model VARCHAR(255),
    year INTEGER,
    description VARCHAR(255),
    status BOOLEAN
)''')

cursor.execute(f'''INSERT INTO cars(mark, model, year, description, status) VALUES("Tesla", "Model X", 2020, "kjdbfaisbdfabs", True)''')
connect.commit()
# connect.close()

def create():
    mark = input("Type mark: ")
    model = input("Type model: ")
    year = int(input("Type year: "))
    description = input("Type description: ")
    status = True
    cursor.execute(f'''INSERT INTO cars(mark, model, year, description, status)
    VALUES("{mark}", "{model}", {year}, "{description}", {status})''')
    connect.commit()
    # connect.close()

def update():
    cursor.execute('''SELECT * FROM cars''')
    data = cursor.fetchall()

    for i in data:
        print(f"ID: {i[0]}, Mark: {i[1]}, Model: {i[2]}, Year: {i[3]}, Description: {i[4]}, Status: {i[5]}")
        print("====================================================================================================================================")

    a = int(input("Which one wanna change(ID): "))
    for i in data:
        if i[0] == a:
            print(f"ID: {i[0]}, Mark: {i[1]}, Model: {i[2]}, Year: {i[3]}, Description: {i[4]}, Status: {i[5]}")
            print("====================================================================================================================================")
            print("1 - Mark, 2 - Model, 3 - Year, 4 - Description, 5 - Status")
            b = int(input("What wanna change: "))
            if b == 1:
                i[1] = input("Type mark: ")
                # print(i)
            elif b == 2:
                i[2] = input("Type model: ")
            elif b == 3:
                i[3] = int(input("Type year: "))
            elif b == 4:
                i[4] = input("Type description: ")
            elif b == 5:
                c = input("1 - True : 2 - False: ")
                if c == 1:
                    i[5] = True
                elif c == 2:
                    i[5] = False
            else:
                print("Type correctly!")
        else:
            print("Type correctly!")


def status_view():
    cursor.execute('''SELECT * FROM cars''')
    data = cursor.fetchall()

    for i in data:
        if i[5] == True:
            print(f"ID: {i[0]}, Mark: {i[1]}, Model: {i[2]}, Year: {i[3]}, Description: {i[4]}, Status: {i[5]}")
            print("====================================================================================================================================")

create()
update()
status_view()        