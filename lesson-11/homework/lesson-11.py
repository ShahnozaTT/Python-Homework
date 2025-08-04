# Homework:
# 1. Create your own virtual environment and install some python packages.


# pip install requests pandas

# Package    Version

# pandas     2.x.x
# requests   2.x.x

# pip freeze > requirements.txt





# 2. Create custom modules.
#     - Create math_operations.py module. Define `add`, `subtract`, `multiply` and `divide` functions in it.
#    (All functions accept two arguments in this task)
#     - Create string_utils.py module. Define `reverse_string` and `count_vowels` functions in it.
#    (All functions accept one argument in this task)

# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels

# Ввод чисел для математических операций
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print(f"\nСложение: {add(a, b)}")
print(f"Вычитание: {subtract(a, b)}")
print(f"Умножение: {multiply(a, b)}")
print(f"Деление: {divide(a, b)}")

# Ввод строки для строковых функций
text = input("\nВведите строку для обработки: ")

print(f"Строка наоборот: {reverse_string(text)}")
print(f"Количество гласных в строке: {count_vowels(text)}")



# 3. Create custom packages.
#     - Create `geometry` package. 
#     <pre>
#     geometry\
#         __init__.py
#         circle.py
#     </pre>
#     Define `calculate_area` and `calculate_circumference` functions in circle.py.
#        These functions accept one argument(radius).
#     - Create `file_operations` package.
#     <pre>
#     file_operations\
#         __init__.py
#         file_reader.py
#         file_writer.py
#     </pre>
#     Define `read_file` function in file_reader.py. This function accepts one argument(file_path). 
# Define `write_file` function in file_writer.py. This function accepts two arguments(file_path, content).