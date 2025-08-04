# # Homework:

# # Object-Oriented Programming (OOP) Exercises

# ## 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

# import math  # Чтобы использовать значение pi

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# # Тестирование класса
# circle1 = Circle(5)
# print(f"Площадь круга: {circle1.area():.2f}")
# print(f"Периметр круга: {circle1.perimeter():.2f}")



# ## 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. 
# Implement a method to determine the person's age.

# from datetime import datetime

# class Person:
#     def __init__(self, name, country, birth_year, birth_month, birth_day):
#         self.name = name
#         self.country = country
#         self.date_of_birth = datetime(birth_year, birth_month, birth_day)

#     def get_age(self):
#         today = datetime.today()
#         age = today.year - self.date_of_birth.year
#         # Проверка: был ли день рождения в этом году
#         if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age

# # Тестирование
# person1 = Person("Ali", "Uzbekistan", 2000, 5, 15)
# print(f"{person1.name} is {person1.get_age()} years old.")

# person2 = Person("Malika", "Uzbekistan", 2010, 8, 20)
# print(f"{person2.name} is {person2.get_age()} years old.")


# ## 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

# a = int(input("Enter a number a: "))
# b = int(input("Enter a number b: "))

# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             return "Ошибка: деление на ноль!"
#         return a / b

# calc = Calculator()

# print(f"Сложение: {calc.add(a, b)}")
# print(f"Вычитание: {calc.subtract(a, b)}")
# print(f"Умножение: {calc.multiply(a, b)}")
# print(f"Деление: {calc.divide(a, b)}")





# ## 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

# import math

# # Родительский класс
# class Shape:
#     def area(self):
#         pass  # Пока ничего не делает
    
#     def perimeter(self):
#         pass  # Пока ничего не делает

# # Подкласс Circle
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# # Подкласс Square
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

#     def perimeter(self):
#         return 4 * self.side

# # Подкласс Triangle (равносторонний)
# class Triangle(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return (math.sqrt(3) / 4) * (self.side ** 2)

#     def perimeter(self):
#         return 3 * self.side

# # --- Ввод данных от пользователя ---
# radius = float(input("Введите радиус круга: "))
# square_side = float(input("Введите сторону квадрата: "))
# triangle_side = float(input("Введите сторону треугольника: "))

# # --- Создание объектов ---
# circle = Circle(radius)
# square = Square(square_side)
# triangle = Triangle(triangle_side)

# # --- Вывод результатов ---
# print(f"\nCircle area: {circle.area():.2f}, perimeter: {circle.perimeter():.2f}")
# print(f"Square area: {square.area()}, perimeter: {square.perimeter()}")
# print(f"Triangle area: {triangle.area():.2f}, perimeter: {triangle.perimeter()}")




# ## 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree.
#  Include methods for inserting and searching for elements in the binary tree.

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# class BinarySearchTree:
#     def __init__(self):
#         self.root = None  # Сначала дерево пустое

#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert_recursive(self.root, value)

#     def _insert_recursive(self, current_node, value):
#         if value < current_node.value:
#             if current_node.left is None:
#                 current_node.left = Node(value)
#             else:
#                 self._insert_recursive(current_node.left, value)
#         elif value > current_node.value:
#             if current_node.right is None:
#                 current_node.right = Node(value)
#             else:
#                 self._insert_recursive(current_node.right, value)



# ## 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.



# ## 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

# ## 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

# class ShoppingCart:
#     def __init__(self):
#         self.items = {}  # Товары: {item: [price, quantity]}

#     def add_item(self, item, price, quantity):
#         if item in self.items:
#             self.items[item][1] += quantity
#         else:
#             self.items[item] = [price, quantity]
#         print(f"{item} добавлен(о) в корзину ({quantity} шт.)")

#     def remove_item(self, item):
#         if item in self.items:
#             del self.items[item]
#             print(f"{item} удален(о) из корзины.")
#         else:
#             print(f"{item} не найден(о) в корзине.")

#     def calculate_total(self):
#         total = 0
#         for price, quantity in self.items.values():
#             total += price * quantity
#         return total

#     def display_cart(self):
#         if not self.items:
#             print("Корзина пуста.")
#         else:
#             print("Товары в корзине:")
#             for item, (price, quantity) in self.items.items():
#                 print(f"- {item}: {quantity} шт. x {price} = {price * quantity}")
#             print(f"Общая сумма: {self.calculate_total()} сум")

# # --- Основная программа ---
# cart = ShoppingCart()

# while True:
#     action = input("\nВыберите действие (add/remove/display/total/exit): ").strip().lower()

#     if action == 'add':
#         item = input("Введите название товара: ")
#         price = int(input("Введите цену товара: "))
#         quantity = int(input("Введите количество: "))
#         cart.add_item(item, price, quantity)

#     elif action == 'remove':
#         item = input("Введите название товара для удаления: ")
#         cart.remove_item(item)

#     elif action == 'display':
#         cart.display_cart()

#     elif action == 'total':
#         print(f"Общая сумма к оплате: {cart.calculate_total()} сум")

#     elif action == 'exit':
#         print("Выход из программы. Спасибо за покупку!")
#         break

#     else:
#         print("Неверная команда. Попробуйте снова.")


# ## 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.




# ## 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.append(item)
#         print(f"Добавлено в очередь: {item}")
#         self.display()

#     def dequeue(self):
#         if not self.items:
#             print("Очередь пустая, нечего удалять!")
#             return None
#         removed_item = self.items.pop(0)
#         print(f"Удалено из очереди: {removed_item}")
#         self.display()
#         return removed_item

#     def display(self):
#         if not self.items:
#             print("Очередь пустая.")
#         else:
#             print("Текущая очередь (слева направо):", self.items)

# # --- Тестирование ---
# queue = Queue()

# queue.enqueue("Клиент 1")
# queue.enqueue("Клиент 2")
# queue.enqueue("Клиент 3")

# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()  # Попробуем удалить из пустой очереди




# ## 11. Bank Class
# Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance):
        if account_number in self.accounts:
            print(f"Аккаунт {account_number} уже существует.")
        else:
            self.accounts[account_number] = {"name": name, "balance": initial_balance}
            print(f"Аккаунт {account_number} создан для {name} с балансом {initial_balance} сум.")

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print(f"Аккаунт {account_number} не найден.")
        else:
            self.accounts[account_number]["balance"] += amount
            print(f"Пополнение: {amount} сум. Новый баланс: {self.accounts[account_number]['balance']} сум.")

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            print(f"Аккаунт {account_number} не найден.")
        else:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f"Снятие: {amount} сум. Остаток: {self.accounts[account_number]['balance']} сум.")
            else:
                print(f"Недостаточно средств. Баланс: {self.accounts[account_number]['balance']} сум.")

    def display_account(self, account_number):
        if account_number not in self.accounts:
            print(f"Аккаунт {account_number} не найден.")
        else:
            acc = self.accounts[account_number]
            print(f"--- Информация об аккаунте ---\nНомер: {account_number}\nИмя: {acc['name']}\nБаланс: {acc['balance']} сум\n")

# --- Основная программа ---
bank = Bank()

while True:
    print("\nВыберите действие:")
    print("1. Создать аккаунт")
    print("2. Пополнить счёт")
    print("3. Снять средства")
    print("4. Показать данные аккаунта")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        acc_num = int(input("Введите номер аккаунта: "))
        name = input("Введите имя владельца: ")
        balance = int(input("Введите начальный баланс: "))
        bank.create_account(acc_num, name, balance)

    elif choice == '2':
        acc_num = int(input("Введите номер аккаунта для пополнения: "))
        amount = int(input("Введите сумму пополнения: "))
        bank.deposit(acc_num, amount)

    elif choice == '3':
        acc_num = int(input("Введите номер аккаунта для снятия: "))
        amount = int(input("Введите сумму для снятия: "))
        bank.withdraw(acc_num, amount)

    elif choice == '4':
        acc_num = int(input("Введите номер аккаунта для просмотра: "))
        bank.display_account(acc_num)

    elif choice == '5':
        print("Выход из программы. Спасибо за использование банка!")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")
