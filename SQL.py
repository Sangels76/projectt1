import sqlite3
import random


conn = sqlite3.connect('users.dn')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    login VARCHAR(50),
    password TEXT,
    balance INTEGER(7)
)
""")


def register_user():
    print("Добро пожаловать в меню регистрации!")
    login = input("Введите логин:")
    password = input("Введите пароль:")
    balance = round(random.uniform(1000, 10000))

    cursor.execute("""
            INSERT INTO users (login, password, balance)
            VALUES (?,?,?)""", (login, password, balance)
                   )
    conn.commit()
    print(f"Пользователь {login} успешно зарегистрирован!\n"
          f"Ваш баланс: {balance}\n")


register_user()




