from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from faker import Faker

# Підключення до MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["cat_database"]
    collection = db["cats"]
    print("Connected to MongoDB")
except errors.ConnectionError as e:
    print(f"Could not connect to MongoDB: {e}")


# Створення екземпляру Faker
fake = Faker()

# Функція для створення випадкових даних про котів
def create_fake_cat():
    return {
        "name": fake.first_name(),
        "age": fake.random_int(min=1, max=15),
        "features": [fake.word() for _ in range(3)]
    }

# Додавання 10 випадкових документів у колекцію
for _ in range(10):
    cat = create_fake_cat()
    collection.insert_one(cat)

print("Inserted 10 fake cats into the database.")


# Функція для створення запису
def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Created cat with id: {result.inserted_id}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

# Функція для виведення всіх записів
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

# Функція для виведення інформації про кота за ім'ям
def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"No cat found with the name {name}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

# Функція для оновлення віку кота за ім'ям
def update_cat_age_by_name(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Updated age of {name} to {new_age}")
        else:
            print(f"No cat found with the name {name}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

# Функція для додавання нової характеристики до списку features за ім'ям
def add_feature_by_name(name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"Added feature '{new_feature}' to cat {name}")
        else:
            print(f"No cat found with the name {name}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

# Функція для видалення запису за ім'ям
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Deleted cat with the name {name}")
        else:
            print(f"No cat found with the name {name}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

# Функція для видалення всіх записів
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

# Приклад використання функцій
if __name__ == "__main__":
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    read_all_cats()
    print("All cats:")
    read_cat_by_name("barsik")
    print("\nCat with name 'barsik':")
    update_cat_age_by_name("barsik", 4)
    print("\nUpdating age of 'barsik' to 4:")
    add_feature_by_name("barsik", "муркоче")
    print("\nAdding feature 'friendly' to 'barsik':")
    read_cat_by_name("barsik")
    print("\nCat with name 'barsik':")
    delete_cat_by_name("barsik")
    print("\nDeleting cat 'barsik':")
    read_all_cats()
    print("All cats:")
    delete_all_cats()
    print("\nDeleting all cats:")
   
