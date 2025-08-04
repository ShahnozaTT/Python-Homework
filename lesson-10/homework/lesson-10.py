# ## Homework Projects:

# Homework 1. ToDo List Application

# 1. Define Task Class:
#     - Create a Task class with attributes such as task title, description, due date, and status.
# 2. Define ToDoList Class:
#     - Create a ToDoList class that manages a list of tasks.
#     - Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
# 3. Create Main Program:
#     - Develop a simple CLI to interact with the ToDoList.
#     - Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
# 4. Test the Application:
#     - Create instances of tasks and test the functionality of your ToDoList.

# class Task:
#     def __init__(self, title, description, due_date):
#         self.title = title
#         self.description = description
#         self.due_date = due_date
#         self.completed = False  # Статус выполнения задачи (по умолчанию False)

#     def mark_complete(self):
#         self.completed = True  # Помечаем задачу как выполненную

#     def __str__(self):
#         status = "✅ Выполнено" if self.completed else "❌ Не выполнено"
#         return f"Заголовок: {self.title}\nОписание: {self.description}\nСрок: {self.due_date}\nСтатус: {status}\n"

# class ToDoList:
#     def __init__(self):
#         self.tasks = []  # Список для хранения задач

#     def add_task(self, task):
#         self.tasks.append(task)
#         print(f"Задача '{task.title}' добавлена!")

#     def list_all_tasks(self):
#         if not self.tasks:
#             print("Список задач пуст.")
#         else:
#             for i, task in enumerate(self.tasks, 1):
#                 print(f"--- Задача {i} ---")
#                 print(task)

#     def list_incomplete_tasks(self):
#         incomplete_tasks = [task for task in self.tasks if not task.completed]
#         if not incomplete_tasks:
#             print("Нет невыполненных задач.")
#         else:
#             for i, task in enumerate(incomplete_tasks, 1):
#                 print(f"--- Задача {i} ---")
#                 print(task)

#     def mark_task_complete(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index].mark_complete()
#             print(f"Задача '{self.tasks[index].title}' отмечена как выполненная.")
#         else:
#             print("Неверный номер задачи.")

# todo_list = ToDoList()

# while True:
#     print("\nВыберите действие:")
#     print("1. Добавить задачу")
#     print("2. Отметить задачу как выполненную")
#     print("3. Показать все задачи")
#     print("4. Показать только невыполненные задачи")
#     print("5. Выйти")

#     choice = input("Введите номер действия: ")

#     if choice == '1':
#         title = input("Введите заголовок задачи: ")
#         description = input("Введите описание задачи: ")
#         due_date = input("Введите срок выполнения: ")
#         task = Task(title, description, due_date)
#         todo_list.add_task(task)

#     elif choice == '2':
#         todo_list.list_all_tasks()
#         index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
#         todo_list.mark_task_complete(index)

#     elif choice == '3':
#         todo_list.list_all_tasks()

#     elif choice == '4':
#         todo_list.list_incomplete_tasks()

#     elif choice == '5':
#         print("Выход из программы.")
#         break

#     else:
#         print("Неверный выбор. Попробуйте снова.")




# Homework 2. Simple Blog System

# 1. Define Post Class:
#     - Create a Post class with attributes like title, content, and author.
# 2. Define Blog Class:
#     - Create a Blog class that manages a list of posts.
#     - Include methods to add a post, list all posts, and display posts by a specific author.
# 3. Create Main Program:
#     - Develop a CLI to interact with the Blog system.
#     - Include options to add posts, list all posts, and display posts by a specific author.
# 4. Enhance Blog System:
#     - Add functionality to delete a post, edit a post, and display the latest posts.
# 5. Test the Application:
#     - Create instances of posts and test the functionality of your Blog system.

# 


# class Post:
#     def __init__(self, title, content, author):
#         self.title = title
#         self.content = content
#         self.author = author

#     def __str__(self):
#         return f"Заголовок: {self.title}\nАвтор: {self.author}\nСодержание: {self.content}\n"


# class Blog:
#     def __init__(self):
#         self.posts = []

#     def add_post(self, post):
#         self.posts.append(post)
#         print(f"Пост '{post.title}' добавлен.")

#     def list_all_posts(self):
#         if not self.posts:
#             print("Нет опубликованных постов.")
#         else:
#             for i, post in enumerate(self.posts, 1):
#                 print(f"--- Пост {i} ---")
#                 print(post)

#     def list_posts_by_author(self, author):
#         filtered_posts = [post for post in self.posts if post.author.lower() == author.lower()]
#         if not filtered_posts:
#             print(f"Нет постов автора '{author}'.")
#         else:
#             for i, post in enumerate(filtered_posts, 1):
#                 print(f"--- Пост {i} ---")
#                 print(post)

#     def delete_post(self, index):
#         if 0 <= index < len(self.posts):
#             removed = self.posts.pop(index)
#             print(f"Пост '{removed.title}' удалён.")
#         else:
#             print("Неверный номер поста.")

#     def edit_post(self, index, new_title=None, new_content=None):
#         if 0 <= index < len(self.posts):
#             if new_title:
#                 self.posts[index].title = new_title
#             if new_content:
#                 self.posts[index].content = new_content
#             print(f"Пост отредактирован.")
#         else:
#             print("Неверный номер поста.")

#     def latest_posts(self, count=3):
#         print(f"Последние {count} постов:")
#         for post in self.posts[-count:][::-1]:  # последние N постов в обратном порядке
#             print(post)

# blog = Blog()

# while True:
#     print("\nВыберите действие:")
#     print("1. Добавить пост")
#     print("2. Показать все посты")
#     print("3. Показать посты по автору")
#     print("4. Удалить пост")
#     print("5. Редактировать пост")
#     print("6. Показать последние посты")
#     print("7. Выйти")

#     choice = input("Введите номер действия: ")

#     if choice == '1':
#         title = input("Введите заголовок поста: ")
#         content = input("Введите содержание поста: ")
#         author = input("Введите имя автора: ")
#         post = Post(title, content, author)
#         blog.add_post(post)

#     elif choice == '2':
#         blog.list_all_posts()

#     elif choice == '3':
#         author = input("Введите имя автора: ")
#         blog.list_posts_by_author(author)

#     elif choice == '4':
#         blog.list_all_posts()
#         index = int(input("Введите номер поста для удаления: ")) - 1
#         blog.delete_post(index)

#     elif choice == '5':
#         blog.list_all_posts()
#         index = int(input("Введите номер поста для редактирования: ")) - 1
#         new_title = input("Введите новый заголовок (или Enter для пропуска): ")
#         new_content = input("Введите новое содержание (или Enter для пропуска): ")
#         blog.edit_post(index, new_title if new_title else None, new_content if new_content else None)

#     elif choice == '6':
#         count = int(input("Сколько последних постов вывести? "))
#         blog.latest_posts(count)

#     elif choice == '7':
#         print("Выход из программы.")
#         break

#     else:
#         print("Неверный выбор. Попробуйте снова.")










# Homework 3. Simple Banking System

# 1. Define Account Class:
#     - Create an Account class with attributes like account number, account holder name, and balance.
# 2. Define Bank Class:
#     - Create a Bank class that manages a list of accounts.
#     - Include methods to add an account, check balance, deposit money, and withdraw money.
# 3. Create Main Program:
#     - Develop a CLI to interact with the Banking system.
#     - Include options to add accounts, check balance, deposit money, and withdraw money.
# 4. Enhance Banking System:
#     - Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
# 5. Test the Application:
#     - Create instances of accounts and test the functionality of your Banking system.

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