# Homework:
# 1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

# from datetime import date, datetime, timedelta

# today = date.today()

# birth_str = input("Enter your birthday (YYYY-MM-DD): ")
# birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()

# # Вычисляем полные годы
# years = today.year - birth_date.year

# # Если день рождения ещё не наступил в этом году — уменьшаем год на 1
# if (today.month, today.day) < (birth_date.month, birth_date.day):
#     years -= 1

# # Вычисляем месяцы
# months = today.month - birth_date.month
# if today.day < birth_date.day:
#     months -= 1
# if months < 0:
#     months += 12

# # Вычисляем дни
# if today.day >= birth_date.day:
#     days = today.day - birth_date.day
# else:
#     prev_month_last_day = today.replace(day=1) - timedelta(days=1)
#     days = prev_month_last_day.day - birth_date.day + today.day

# # Результат
# print(f"You are {years} years, {months} months, and {days} days old.")



# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

# from datetime import datetime, date

# # 1. Ввод даты рождения
# birth_str = input("Введите дату рождения (в формате YYYY-MM-DD): ")
# birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()

# # 2. Сегодня
# today = date.today()

# # 3. Дата следующего дня рождения
# next_birthday = date(today.year, birth_date.month, birth_date.day)

# # 4. Если в этом году ДР уже был — переносим на следующий год
# if next_birthday < today:
#     next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

# # 5. Разница в днях
# days_left = (next_birthday - today).days

# # 6. Вывод
# print(f"До следующего дня рождения осталось {days_left} дней.")




# 3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. 
# Calculate and print the date and time when the meeting will end.

# from datetime import datetime, timedelta

# # 1. Ввод текущей даты и времени
# current_str = input("Введите текущую дату и время (YYYY-MM-DD HH:MM): ")
# current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")

# # 2. Ввод длительности встречи
# hours = int(input("Введите количество часов: "))
# minutes = int(input("Введите количество минут: "))

# # 3. Вычисление времени окончания
# meeting_duration = timedelta(hours=hours, minutes=minutes)
# end_time = current_dt + meeting_duration

# # 4. Вывод
# print("Встреча закончится:", end_time.strftime("%Y-%m-%d %H:%M"))


# 4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, 
# and then convert and print the date and time in another timezone of their choice.

# from datetime import datetime, timedelta

# # 1. Исходные данные (можно менять для теста)
# date_str = "2025-08-09 18:00"   # Дата и время в исходном поясе
# source_offset = 5               # Смещение от UTC (например, Ташкент UTC+5)
# target_offset = -4              # Смещение от UTC (например, Нью-Йорк UTC-4)

# # 2. Преобразуем в datetime
# from datetime import datetime, timedelta

# # 1. Берём текущую дату и время
# now = datetime.now()
# source_offset = 5    # Ваш часовой пояс, например Ташкент UTC+5
# target_offset = -4   # Целевой часовой пояс, например Нью-Йорк UTC-4

# # 2. Переводим в UTC
# utc_time = now - timedelta(hours=source_offset)

# # 3. Переводим в целевой часовой пояс
# target_time = utc_time + timedelta(hours=target_offset)

# # 4. Вывод
# print(f"Текущее время: {now.strftime('%Y-%m-%d %H:%M')} (UTC{source_offset:+})")
# print(f"Время в целевом поясе: {target_time.strftime('%Y-%m-%d %H:%M')} (UTC{target_offset:+})")



# 5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time 
# remaining until that point in regular intervals (e.g., every second).

# from datetime import datetime
# import time

# # 1. Будущая дата (можно ввести или зашить в код)
# future_time = datetime(2025, 8, 10, 12, 0, 0)  # год, месяц, день, час, минута, секунда

# while True:
#     # 2. Текущее время
#     now = datetime.now()
    
#     # 3. Разница
#     remaining = future_time - now
    
#     # 4. Если время вышло — стоп
#     if remaining.total_seconds() <= 0:
#         print("Время вышло!")
#         break
    
#     # 5. Дни, часы, минуты, секунды
#     days = remaining.days
#     hours, remainder = divmod(remaining.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)
    
#     print(f"Осталось: {days} дн {hours:02}:{minutes:02}:{seconds:02}")
    
#     # 6. Ждём 1 секунду
#     time.sleep(1)


# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

# import re

# # 1. Тестовый email (можно заменить input())
# email = "example@mail.com"

# # 2. Регулярное выражение для проверки email
# pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# # 3. Проверка
# if re.match(pattern, email):
#     print("Email валиден ✅")
# else:
#     print("Email НЕвалиден ❌")


# 7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. 
# For example, convert "1234567890" to "(123) 456-7890".

# # 1. Ввод номера телефона
# phone = input("Введите номер телефона из 10 цифр: ")

# # 2. Проверка длины и цифр
# if len(phone) == 10 and phone.isdigit():
#     # 3. Форматирование
#     formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
#     print("Отформатированный номер:", formatted)
# else:
#     print("Ошибка: номер должен содержать ровно 10 цифр.")


# 8. Password Strength Checker: Implement a password strength checker. 
# Ask the user to input a password and check if it meets certain criteria (e.g., minimum length,
#  contains at least one uppercase letter, one lowercase letter, and one digit).

# password = input("Введите пароль: ")

# if len(password) < 8:
#     print("Пароль слишком короткий, минимум 8 символов.")
# elif not any(c.isupper() for c in password):
#     print("В пароле должна быть хотя бы одна заглавная буква.")
# elif not any(c.islower() for c in password):
#     print("В пароле должна быть хотя бы одна строчная буква.")
# elif not any(c.isdigit() for c in password):
#     print("В пароле должна быть хотя бы одна цифра.")
# else:
#     print("Пароль надёжный ✅")



# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text.
#  Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

# text = """Python — это высокоуровневый язык программирования с динамической типизацией."""
# word = input("Введите слово для поиска: ").lower()

# text_lower = text.lower()

# count = text_lower.count(word)

# print(f"Слово '{word}' встречается {count} раз(а).")


# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, 
# and then identify and print all the dates present in the text.

# import re

# text = input("Введите текст с датами: ")

# # Паттерн для дат в формате 09-08-2025 или 09/08/2025
# date_pattern = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b'

# dates = re.findall(date_pattern, text)

# if dates:
#     print("Найденные даты:")
#     for d in dates:
#         print(d)
# else:
#     print("Даты не найдены.")
