# # Homework:

# # Python Exception Handling: Exercises, Solutions, and Practice

# ## Exception Handling Exercises

# 1. Write a Python program to handle a `ZeroDivisionError` exception when dividing a number by zero.

# try:
#     a = int(input("Birinchi sonni kiriting: "))
#     b = int(input("Ikkinchi sonni kiriting: "))
#     result = a / b
#     print("Natija:", result)
# except ZeroDivisionError:
#     print("Nolga bo‘lish mumkin emas!")



# 2. Write a Python program that prompts the user to input an integer and raises a `ValueError` exception if the input is not a valid integer.

# try:
#     number = int(input("Butun son kiriting: "))
#     print(number)
# except ValueError:
#     print("Butun son kiritish zarur!")


# 3. Write a Python program that opens a file and handles a `FileNotFoundError` exception if the file does not exist.

# filename = input("Fayl nomini kiriting: ")

# try:
#     with open(filename, 'r') as file:
#         content = file.read()
#         print("Fayl mazmuni:")
#         print(content)
# except FileNotFoundError:
#     print("Fayl topilmadi!")




# 4. Write a Python program that prompts the user to input two numbers and raises a `TypeError` exception if the inputs are not numerical.

# try:
#     a = input("Birinchi sonni kiriting: ")
#     b = input("Ikkinchi sonni kiriting: ")

#     if not a.isdigit() or not b.isdigit():
#         raise TypeError("Faqat raqam kiriting!")

#     a = int(a)
#     b = int(b)
#     print("Yig'indi:", a + b)

# except TypeError as e:
#     print(e)


# 5. Write a Python program that opens a file and handles a `PermissionError` exception if there is a permission issue.

# try:
#     with open('secret.txt', 'r') as file:
#         content = file.read()
# except PermissionError:
#     print("Faylga ruxsat yo'q!")



# 6. Write a Python program that executes an operation on a list and handles an `IndexError` exception if the index is out of range.

# my_list = [10, 20, 30]

# try:
#     index = int(input("Indeks kiriting (0-2): "))
#     print("Qiymat: ", my_list [index])
# except IndexError:
#     print("Bunday indeks mavjud emas!")



# 7. Write a Python program that prompts the user to input a number and handles a `KeyboardInterrupt` exception if the user cancels the input.

# try:
#     number = int(input("Son kiriting: "))
#     print("Siz kiritgan son:", number)
# except KeyboardInterrupt:
#     print("\nInput bekor qilindi!")




# 8. Write a Python program that executes division and handles an `ArithmeticError` exception if there is an arithmetic error.

# try:
#     a = int(input("Birinchi sonno kiriting: "))
#     b = int(input("Ikkinchi sonni kiriting: "))
#     result = a/b
#     print("Natija: ", result)
# except ArithmeticError:
#     print("Aritmetik xatolik yuz berdi!")

# 9. Write a Python program that opens a file and handles a `UnicodeDecodeError` exception if there is an encoding issue.

# filename = input("Fayl nomini kiriting: ")

# try:
#     with open(filename, 'r', encoding='ascii') as file:
#         content = file.read()
#         print("Fayl mazmuni:")
#         print(content)
# except UnicodeDecodeError:
#     print("Kodlashdagi xatolik yuz berdi!")
# except FileNotFoundError:
#     print("Fayl topilmadi!")



# 10. Write a Python program that executes a list operation and handles an `AttributeError` exception if the attribute does not exist.

# my_list = [1, 2, 3]

# try:
#     my_list.upper()  # Ошибка: у списка нет метода upper()
# except AttributeError:
#     print("Bunday atribut mavjud emas!")




# # Python File Input Output: Exercises, Practice, Solution

# ## File Input/Output Exercises

# 1. Write a Python program to read an entire text file.

# filename = input("Fayl nomini kiriting: ")

# try:
#     with open(filename, 'r', encoding='utf-8') as file:
#         content = file.read()
#         print("Fayl mazmuni:")
#         print(content)
# except FileNotFoundError:
#     print("Fayl topilmadi!")




# 2. Write a Python program to read first `n` lines of a file.

# def read_first_n_lines(filename, n):
#     try:
#         with open(filename, 'r') as file:
#             for index, line in enumerate(file):
#                 if index >= n:
#                     break
#                 print(line.strip())
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# filename = 'example.txt'
# n = int(input("Enter the number of lines to read: "))
# read_first_n_lines(filename, n)


# 3. Write a Python program to append text to a file and display the text.

# def append_text_to_file(filename, text):
#     try:
#         # Открываем файл в режиме добавления ('a')
#         with open(filename, 'a') as file:
#             file.write(text + '\n')  # Добавляем текст и перевод строки
#         print("Text appended successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def display_file_content(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()  # Читаем всё содержимое файла
#             print("\n--- File Content ---")
#             print(content)
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# filename = 'example.txt'
# text_to_append = input("Enter text to append to the file: ")

# append_text_to_file(filename, text_to_append)
# display_file_content(filename)




# 4. Write a Python program to read last `n` lines of a file.


# def read_last_n_lines(filename, n):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()  # Считываем все строки в список
#             for line in lines[-n:]:   # Берём срез последних n строк
#                 print(line.strip())
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# filename = 'example.txt'
# n = int(input("Enter the number of lines to read from the end: "))
# read_last_n_lines(filename, n)


# 5. Write a Python program to read a file line by line and store it into a list.

# def read_file_to_list(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             return [line.strip() for line in lines]
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         return []
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []   
    

# 6. Write a Python program to read a file line by line and store it into a variable.

# def read_file_to_variable(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             return content
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         return ""
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return ""           

# 7. Write a Python program to read a file line by line and store it into an array.

# def read_file_to_array(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             return [line.strip() for line in lines]
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         return []
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []

# 8. Write a Python program to find the longest words.

# def find_longest_words(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             words = content.split()
#             max_length = max(len(word) for word in words)
#             longest_words = [word for word in words if len(word) == max_length]
#             return longest_words
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         return []
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []   

# 9. Write a Python program to count the number of lines in a text file.

# def count_lines_in_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             return len(lines)
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         return 0
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return 0

# 10. Write a Python program to count the frequency of words in a file.

# def count_word_frequency(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             words = content.split()
#             frequency = {}
#             for word in words:
#                 frequency[word] = frequency.get(word, 0) + 1
#             return frequency
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         return {}
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return {}

# 11. Write a Python program to get the file size of a plain file.

# def get_file_size(filename):    
#     try:
#         import os
#         size = os.path.getsize(filename)
#         return size
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         return 0
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return 0


# 12. Write a Python program to write a list to a file.

# def write_list_to_file(filename, data_list):
#     try:
#         with open(filename, 'w') as file:
#             for item in data_list:
#                 file.write(item + '\n')  # Записываем элемент + перевод строки
#         print(f"List has been written to '{filename}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# filename = 'output.txt'
# data = ['Apple', 'Banana', 'Cherry', 'Date']

# write_list_to_file(filename, data)




# 13. Write a Python program to copy the contents of a file to another file.

# def copy_file(source_file, destination_file):
#     try:
#         with open(source_file, 'r') as src:
#             content = src.read()  # Читаем всё содержимое исходного файла

#         with open(destination_file, 'w') as dest:
#             dest.write(content)  # Записываем содержимое в целевой файл

#         print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
#     except FileNotFoundError:
#         print(f"File '{source_file}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# source = 'source.txt'
# destination = 'destination.txt'
# copy_file(source, destination)




# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.

# 15. Write a Python program to read a random line from a file.

# 16. Write a Python program to assess if a file is closed or not.

# 17. Write a Python program to remove newline characters from a file.

# 18. Write a Python program that takes a text file as input and returns the number of words in a given text file.
#    - **Note:** Some words can be separated by a comma with no space.

# 19. Write a Python program to extract characters from various text files and put them into a list.

# 20. Write a Python program to generate 26 text files named `A.txt`, `B.txt`, and so on up to `Z.txt`.

# 21. Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

