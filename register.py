import random
from connect_db import Database
import login


def register():
    print("Register Page")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone Number: ")
    generated_number = random.randint(1000, 9999)
    print(f"\nGeneratsiya qilingan raqam: {generated_number}\n")

    while True:
        entered_number = int(input("Generatsiya qilingan raqamni kiriting: "))
        if entered_number == generated_number:
            query = "SELECT username FROM users"
            data = Database.connect(query, "select")
            username = input("Username: ")
            for i in data:
                if username == i[0]:
                    print("Bunday username mavjud")
                    username = input("Username: ")
            password = input("Password: ")
            print("Sizning foydalanuvchi nomingiz:", username)
            print("Sizning parolingiz:", password)
            break
        else:
            print("Noto'g'ri raqam. Qayta kiriting.")



    query = f"""INSERT INTO users(first_name, last_name, username, password, phone_number) 
    VALUES('{first_name}', '{last_name}', '{username}', '{password}', '{phone_number}')"""

    print(Database.connect(query, "insert"))
    return login.login()