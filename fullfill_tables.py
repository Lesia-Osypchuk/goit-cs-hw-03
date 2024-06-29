from faker import Faker
import random
import psycopg2
from psycopg2 import sql

# Параметри підключення до бази даних PostgreSQL
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "Anna050319771"
DB_HOST = "localhost"
DB_PORT = "5432"

# Ініціалізуємо Faker для генерації випадкових даних
fake = Faker()

# З'єднання з базою даних
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Підключено до бази даних PostgreSQL")
except psycopg2.Error as e:
    print("Помилка підключення до бази даних PostgreSQL:", e)
    exit()

# Створення курсора для виконання SQL-запитів
cur = conn.cursor()

try:
    # Заповнення таблиці users
    for _ in range(10):  # Приклад: генеруємо 10 користувачів
        fullname = fake.name()
        email = fake.email()

        # Вставка даних в таблицю users
        cur.execute(
            sql.SQL("INSERT INTO users (fullname, email) VALUES (%s, %s)"),
            (fullname, email)
        )

    # Заповнення таблиці status
    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cur.execute(
            sql.SQL("INSERT INTO status (name) VALUES (%s)"),
            [status]
        )

    # Заповнення таблиці tasks
    for _ in range(20):  # Приклад: генеруємо 20 завдань
        title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        description = fake.text()
        status_id = random.randint(1, len(statuses))  # Випадковий статус
        user_id = random.randint(1, 10)  # Випадковий користувач

        # Вставка даних в таблицю tasks
        cur.execute(
            sql.SQL("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)"),
            (title, description, status_id, user_id)
        )

    # Підтвердження та збереження змін у базі даних
    conn.commit()
    print("Дані успішно додані до таблиць")

except psycopg2.Error as e:
    print("Помилка виконання SQL-запиту:", e)
finally:
    # Закриття курсора та з'єднання з базою даних
    cur.close()
    conn.close()
    print("З'єднання з базою даних закрито")
