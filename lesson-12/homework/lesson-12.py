# Homework:

# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

# import threading

# # Функция для проверки простого числа
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Потоковая функция
# def check_primes_in_range(start, end, result, lock):
#     primes = []
#     for number in range(start, end + 1):
#         if is_prime(number):
#             primes.append(number)
#     # Блокируем доступ к общему ресурсу перед записью
#     with lock:
#         result.extend(primes)

# # Главная программа
# def threaded_prime_checker(start_range, end_range, num_threads):
#     threads = []
#     result = []
#     lock = threading.Lock()
#     range_size = (end_range - start_range + 1) // num_threads

#     for i in range(num_threads):
#         start = start_range + i * range_size
#         end = start + range_size - 1 if i != num_threads - 1 else end_range
#         thread = threading.Thread(target=check_primes_in_range, args=(start, end, result, lock))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

#     result.sort()
#     print(f"Primes between {start_range} and {end_range}: {result}")

# # Пример запуска
# threaded_prime_checker(1, 100, 4)






# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.

import threading
from collections import defaultdict

# Потоковая функция для обработки части текста
def process_lines(lines, result_dict, lock):
    local_counter = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        for word in words:
            cleaned_word = word.lower().strip('.,!?()[]{}"\'')  # чистим от знаков препинания
            local_counter[cleaned_word] += 1

    # Сливаем локальные результаты в общий словарь
    with lock:
        for word, count in local_counter.items():
            result_dict[word] += count

# Главная программа
def threaded_word_count(file_path, num_threads):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    result_dict = defaultdict(int)
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i != num_threads - 1 else total_lines
        thread = threading.Thread(target=process_lines, args=(lines[start:end], result_dict, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Вывод результата
    for word, count in sorted(result_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

# Пример запуска
# Создай файл 'sample_text.txt' с текстом для проверки.
threaded_word_count('sample_text.txt', 4)
