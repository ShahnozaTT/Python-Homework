# # Homeworks

# ## 1. Modify String with Underscores
# Given a string `txt`, insert an underscore (`_`) after every third character. 
# If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

# ### Examples
# **Input:** `hello`
# **Output:** `hel_lo`

# **Input:** `assalom`
# **Output:** `ass_alom`

# **Input:** `abcabcabcdeabcdefabcdefg`
# **Output:** `abc_abc_abcd_abcd_abcdef`

# def insert_underscores(text):
#     vowels = 'aeiou'         
#     result = ''              
#     count = 0                
#     i = 0                    

#     while i < len(text):
#         result += text[i]    
#         count += 1           

#         if count == 3:       
#             if text[i] in vowels:
#                 if i + 1 < len(text):
#                     result += text[i + 1] + '_'
#                     i += 1  
#             else:
#                 result += '_'

#             count = 0  
#         i += 1  

#     if result.endswith('_'):
#         result = result[:-1]

#     return result

# print(insert_underscores("hello"))          # hel_lo
# print(insert_underscores("assalom"))        # ass_alom
# print(insert_underscores("abcabcabcdeabcdefabcdefg"))  
# → abc_abc_abc_dea_bc_d_efa_bcd_efg

# ## 2. Integer Squares Exercise

# ### Task
# The provided code stub reads an integer, `n`, from STDIN. For all non-negative integers `i` where `0 <= i < n`, print `i^2`.

# ### Example Input
# ```
# 5
# ```

# ### Example Output
# ```
# 0
# 1
# 4
# 9
# 16
# 

# n = int(input('Biror sonni kiriting: '))

# for i in range(n):
#     print(i ** 2)


# ### Input Format
# The first and only line contains the integer, `n`.

# ### Constraints
# - `1 <= n <= 20`

# ### Output Format
# Print `n` lines, one corresponding to each `i^2` where `0 <= i < n`.

# n = int(input('20 gacha biror sonni kiriting: '))

# for i in range(n):
#     print(i ** 2)


# ## 3. Loop-Based Exercises

# ### Exercise 1: Print first 10 natural numbers using a while loop

# i = 1

# while i <= 10:
#     print(i)
#     i += 1


# ### Exercise 2: Print the following pattern
# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# row = 1

# while row <= 5:
#     num = 1
#     while num <= row:
#         print(num, end=' ')
#         num += 1
#     print()
#     row += 1


# ### Exercise 3: Calculate sum of all numbers from 1 to a given number
# **Example:**
# ```
# Enter number 10
# Sum is: 55


# n = int(input('Biror sonni kiriting: '))

# total_sum = 0

# for i in range(1, n+1):
#     total_sum += i

# print('Sum_is: ', total_sum)



# ### Exercise 4: Print multiplication table of a given number
# **Example:**
# ```
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

# n = int(input('Enter a number: '))

# for i in range(1, 11):
#     print(n*i)


# ### Exercise 5: Display numbers from a list using a loop
# **Given:**
# ```python
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
# **Expected Output:**
# ```
# 75
# 150
# 145
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]

# for num in numbers:
#     if num % 5 != 0:
#         continue  # Пропустить числа, не кратные 5

#     if num > 500:
#         break  # Остановить цикл, если число больше 500

#     if num > 150:
#         continue  # Пропустить числа больше 150

#     print(num)


# ### Exercise 6: Count the total number of digits in a number
# **Example:**
# ```
# 75869
# Output: 5
# ```

# n = input('Введите число: ')
# print('Output:', len(n))


# ### Exercise 7: Print reverse number pattern
# ```
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
#

# n = 5  

# for row in range(n, 0, -1):  
#     for num in range(row, 0, -1):  
#         print(num, end=' ')
#     print()  




# ### Exercise 8: Print list in reverse order using a loop
# **Given:**
# ```python
# list1 = [10, 20, 30, 40, 50]
# ```
# **Expected Output:**
# ```
# 50
# 40
# 30
# 20
# 10



list1 = [10, 20, 30, 40, 50]

i = len(list1) - 1  # начинаем с последнего индекса
while i >= 0:
    print(list1[i])
    i -= 1



# ### Exercise 9: Display numbers from -10 to -1 using a for loop
# ```
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
# ```

# for i in range(-10, 0):
#     print(i)




# ### Exercise 10: Display message “Done” after successful loop execution
# **Example:**
# ```python
# 0
# 1
# 2
# 3
# 4
# Done!
# ```
for i in range(5):  # от 0 до 4
    print(i)

print("Done!")

# ### Exercise 11: Print all prime numbers within a range
# **Example:**
# ```
# Prime numbers between 25 and 50:
# 29
# 31
# 37
# 41
# 43
# 47
# ```

start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:  # пропускаем 0 и 1
        is_prime = True
        for i in range(2, num):  # перебираем ВСЕ числа от 2 до num-1
            if num % i == 0:
                is_prime = False  # нашли делитель ➜ не простое
                break
        if is_prime:
            print(num)




# ### Exercise 12: Display Fibonacci series up to 10 terms
# **Example:**
# ```
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
# ```

# n_terms = 10  # сколько чисел вывести

# n1, n2 = 0, 1  # начальные числа Фибоначчи

# print("Fibonacci sequence:")

# for _ in range(n_terms):
#     print(n1, end=' ')
#     nth = n1 + n2  # следующее число = сумма двух предыдущих
#     n1 = n2        # сдвигаем первое число вправо
#     n2 = nth       # новое второе число



# ### Exercise 13: Find the factorial of a given number
# **Example:**
# ```
# 5! = 120
# ```


# n = int(input("Enter a number to calculate its factorial: "))

# factorial = 1

# if n < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     for i in range(1, n + 1):
#         factorial *= i  # factorial = factorial * i
#     print(f"{n}! = {factorial}")

# ---

# ## 4. Return Uncommon Elements of Lists
# ### Task
# Return the elements that are not common between two lists. The order of elements does not matter.

# ### Examples
# - **Input:** `list1 = [1, 1, 2], list2 = [2, 3, 4]`  
#   **Output:** `[1, 1, 3, 4]`

# - **Input:** `list1 = [1, 2, 3], list2 = [4, 5, 6]`  
#   **Output:** `[1, 2, 3, 4, 5, 6]`

# - **Input:** `list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]`  
#   **Output:** `[2, 2, 5]`


list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

result = []

# Check elements from list1
for elem in list1:
    if elem not in list2:
        result.append(elem)

# Check elements from list2
for elem in list2:
    if elem not in list1:
        result.append(elem)

print(result)
