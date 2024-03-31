from connect_db import Database

def create_table():
    users = """
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            username VARCHAR NOT NULL,
            password VARCHAR NOT NULL,
            phone_number VARCHAR,
            create_date TIMESTAMP DEFAULT now())"""

    data = {
        "users": users
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()