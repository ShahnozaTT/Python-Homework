    # Homework Exercises

## 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

# name=input("What is your name?")
# birth_year=int(input("Year of your birth?"))
# current_year = 2025
# age = current_year - birth_year
# print(f"Hello, {name}, you are {age} years old.")
                            


## 2. Extract Car Names
# Extract car names from the following text:

#txt = 'LMaasleitbtui'

txt = 'LMaasleitbtui'.lower()

# m = txt[1]   # 'm'
# a = txt[2]   # 'a'
# l = txt[5]   # 'l'
# i = txt[7]   # 'i'
# b = txt[9]   # 'b'
# u = txt[11]  # 'u'

# word = m + a + l + i + b + u
# print(word)  # → malibu




## 3. Extract Car Names
# Extract car names from the following text:

#txt = 'MsaatmiazD'

# txt = 'MsaatmiazD'.lower()
# m = txt[0]   # 'm'
# a = txt[2]   # 'a'
# z = txt[8]   # 'z'
# d = txt[9]   # 'd'
# a = txt[7]   # 'a'

# word = m + a + z + d + a
# print(word)  

## 4. Extract Residence Area
# Extract the residence area from the following text:

# txt = "I'am John. I am from London"

# start = txt.find("from ") + len("from ")
# area = txt[start:]

# print(area)  


## 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

# string= input("Enter a string: ")
# reversed_string = string[::-1]
# print(reversed_string)



## 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

# string=input("Enter a string: ").lower()
# string = input("Enter a string: ").lower()

# a = string.count('a')
# e = string.count('e')
# i = string.count('i')
# o = string.count('o')
# u = string.count('u')

# total = a + e + i + o + u

# print("Number of vowels:", total)





## 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.


# numbers = input("Enter numbers separated by spaces: ")


# num_list = numbers.split()           
# num_list = [int(n) for n in num_list]  


# max_value = max(num_list)

# print("Maximum value:", max_value)



## 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

# word = input("Enter a word: ").lower()  

# if word == word[::-1]:
#     print("Yes, it is a palindrome")
# else:
#     print("No, it is not a palindrome")




## 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

# email=input("What is your email address? ")
# domain = email.split("@")[1]
# print("Domain:", domain )


## 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.

# import random
# import string


# length = int(input("Enter desired password length: "))


# characters = string.ascii_letters + string.digits + string.punctuation


# password = ''.join(random.choice(characters) for _ in range(length))


# print("Generated password:", password)
