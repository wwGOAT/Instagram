from connect_db import Database
import users
from main import main


def login_2():
    username = input("Username: ")
    while username == "" and username == "":
        print("Bunday yoza olmaysiz")
        username = input("Username: ")
    password = input("Password: ")

    query = "SELECT * FROM users"
    data = Database.connect(query, "select")
    for i in data:
        if username == i[3] and password == i[4]:
            return users.users()

    return main()


def login():
    print("\n<<<<<<<<<<<Login>>>>>>>>>>>>\n")

    query = "SELECT * FROM users"
    return login_2()