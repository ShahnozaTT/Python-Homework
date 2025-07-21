# Homework:
# 1. 
# def is_leap(year): """ Determines whether a given year is a leap year.

# A year is a leap year if:
# - It is divisible by 4, and
# - It is NOT divisible by 100, unless it is also divisible by 400.

# Parameters:
# year (int): The year to be checked.

# Returns:
# bool: True if the year is a leap year, False otherwise.

# def is_leap(year):
#     if not isinstance(year, int):
#         raise ValueError("Year must be an integer.")
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# year_input = int(input("Enter a year: "))


# if is_leap(year_input):
#     print(f"{year_input} is a leap year.")
# else:
#     print(f"{year_input} is not a leap year.")

# 2. Conditional Statements Exercise

# Given an integer, n, perform the following conditional actions:

#     If n is odd, print Weird
#     If n is even and in the inclusive range of 2 to 5, print Not Weird
#     If n is even and in the inclusive range of 6 to 20, print Weird
#     If n is even and greater than 20, print Not Weird

# Input Format

# A single line containing a positive integer, n.
# Constraints

#    1 <= n <= 100

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.
# Sample Input 0


# n = int(input("Enter a number: "))
# 1 <= n <= 100
# if n % 2 == 1:
#     print("Weird")
# elif 2 <= n <= 5:
#     print("Not Weird")
# elif 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")


# 3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.

# Give two solutions.

# Solution 1 with if-else statement.



# a = int(input("Enter a number (a): "))
# b = int(input("Enter a number (b): "))

# start = a if a % 2 == 0 else a + 1  # если a чётное, оставляем; если нет — +1
# end = b if b % 2 == 0 else b - 1    # если b чётное, оставляем; если нет — -1

# if start > end:
#     even_numbers = []
# else:
#     even_numbers = list(range(start, end + 1, 2))

# print(even_numbers)


# Solution 2 without if-else statement

# a = int(input("Enter a number (a): "))
# b = int(input("Enter a number (b): "))

# even_numbers = list(range(a + a % 2, b + 1, 2)) if a <= b else []

# print(even_numbers)

