# Homeworks:
# Python Dictionary and Set Exercises

# Dictionary Exercises

# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.

# my_dict = {'apple': 10, 'banana': 5, 'cherry': 7}

# ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

# print("Ascending:", ascending)
# print("Descending:", descending)



# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.
# Sample Dictionary:

# my_dict = {0: 10, 1: 20}
# my_dict[2] = 30

# print(my_dict)


# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}

# combined = dic1 | dic2 | dic3

# print(combined)


# 4. Generate a Dictionary with Squares

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# Sample Dictionary (n = 5):

# squares = {}

# for x in range(1, 6): 
#     squares[x] = x * x

# print(squares)

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

# squares = {}

# for x in range(1, 16):  
#     squares[x] = x * x

# print(squares)

# Set Exercises
# 1. Create a Set

# my_set={"a", "b", "c", "d", "e", "f"}
# print(my_set)

# Write a Python program to create a set.

# 2. Iterate Over a Set
# Write a Python program to iterate over sets.

# emails = {'a@gmail.com', 'b@gmail.com', 'c@gmail.com'}

# for email in emails:
#     print(f"Sending message to {email}")



# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.

# my_set = {'apple', 'banana'}
# my_set.add('cherry')
# print(my_set) 


# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.

# my_set = {'apple', 'banana', 'cherry'}
# my_set.remove('cherry')
# print(my_set) 


# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.

# bought = {'milk', 'bread', 'eggs'}
# bought.discard('bread')
# print(bought)