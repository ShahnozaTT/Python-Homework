# ## Homework

# 1. Task: JSON Parsing
#     - write a Python script that reads the students.jon JSON file and prints details of each student.

# import json

# with open('students.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# for student in data['students']:
#     print("Имя:", student['name'])
#     print("Возраст:", student['age'])

#     # Берём город из вложенного словаря "address"
#     city = student.get('address', {}).get('city', 'не указан')
#     print("Город:", city)
#     print("---")


# 2. Task: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent)
#    and print relevant information (temperature, humidity, etc.).

# import requests

# my_api = 'b3729715cf64d50681176749c205a090'
# city = 'Tashkent'
# units = 'metric'  # чтобы температура была в °C

# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api}&units={units}"
# r = requests.get(url)

# data = r.json()

# city_name = data["name"]
# temperature = data["main"]["temp"]
# humidity = data["main"]["humidity"]
# wind_speed = data["wind"]["speed"]

# print(f"City: {city_name}")
# print(f"Temperature: {temperature}°C")
# print(f"Humidity: {humidity}%")
# print(f"Wind Speed: {wind_speed} m/s")



# 3. Task: JSON Modification
#    1. Write a program that allows users to add new books, update existing book information,
#  and delete books from the books.json JSON file.

# import json

# # 1. Чтение файла
# with open("books.json", "r") as f:
#     books = json.load(f)

# # 2. Добавление книги
# new_book = {"title": "Book C", "author": "Author C", "year": 2020}
# books.append(new_book)

# # 3. Обновление книги
# for book in books:
#     if book["title"] == "Book B":
#         book["year"] = 2015
#         break

# # 4. Удаление книги
# books = [book for book in books if book["title"] != "Book A"]

# # 5. Сохранение изменений
# with open("books.json", "w") as f:
#     json.dump(books, f, indent=4)

# print("✅ Изменения сохранены в books.json")




# 4. Task: Movie Recommendation System
#    1. Use this url http://www.omdbapi.com/ to fetch information about movies.
#    2. Create a program that asks users for a movie genre and recommends a random movie from that genre.

# import requests
# import random

# api_key = "f09a0ba7"

# genre = input("Введите жанр: ")

# # Список фильмов для примера
# movies = {
#     "Action": ["Inception", "Mad Max: Fury Road", "Die Hard"],
#     "Comedy": ["The Mask", "Superbad", "Home Alone"],
#     "Drama": ["Forrest Gump", "The Godfather", "The Shawshank Redemption"]
# }

# if genre in movies:
#     chosen = random.choice(movies[genre])
#     url = f"http://www.omdbapi.com/?apikey={api_key}&t={chosen}"
#     r = requests.get(url)
#     data = r.json()

#     print(f"🎬 {data['Title']} ({data['Year']})")
#     print(f"Жанр: {data['Genre']}")
#     print(f"Режиссёр: {data['Director']}")
#     print(f"Сюжет: {data['Plot']}")
# else:
#     print("❌ Жанр не найден в базе.")


