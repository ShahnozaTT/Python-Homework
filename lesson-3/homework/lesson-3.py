# # Homework: List and Tuple Exercises

# ## 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.


# my_fruits = ["apple", "banana", "cherry", "pear", "strawberry"]
# print(my_fruits[2])  



# ## 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.

# my_list1 = [1, 2, 3]
# my_list2 = [4, 5, 6]
# concatenated_list = my_list1 + my_list2
# print(concatenated_list)


# ## 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

# my_numbers = [12, 24, 35, 56, 67]
# extracted_numbers = [my_numbers[0], my_numbers[len(my_numbers) // 2], my_numbers[-1]]
# print(extracted_numbers)

# ## 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

# my_favorite_movies = ["Inception", "The Matrix", "Interstellar", "Parasite", "The Shawshank Redemption"]
# my_favorite_movies_tuple = tuple(my_favorite_movies)
# print(my_favorite_movies_tuple)

# ## 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

# my_cities = ["New York", "Los Angeles", "Paris", "Tokyo", "London"]
# is_paris_in_list = "Paris" in my_cities
# print(is_paris_in_list)  

# ## 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

# original_list = [1, 2, 3]
# duplicated_list = original_list * 2
# print(duplicated_list) 


# ## 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

# my_list = [10, 20, 30, 40, 50]
# my_list[0], my_list[-1] = my_list[-1], my_list[0]
# print(my_list)  # [50, 20, 30, 40, 10]


# ## 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# slice_tuple = my_tuple[3:8]
# print(slice_tuple)  


# ## 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

# my_colors = ["red", "blue", "green", "blue", "yellow", "blue"]
# blue_count = my_colors.count("blue")
# print(blue_count)  # Output: 3

# ## 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

# my_animals = ("cat", "dog", "lion", "tiger", "elephant")
# lion_index = my_animals.index("lion")
# print(lion_index)  

# ## 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)

# merged_tuple = tuple1 + tuple2
# print(merged_tuple)


# ## 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

# my_list = [1, 2, 3, 4, 5]
# my_tuple = (1, 2, 3, 4, 5)

# print(len(my_list))
# print(len(my_tuple))



# ## 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

# my_tuple = (10, 20, 30, 40, 50)
# my_list_from_tuple = list(my_tuple)
# print(my_list_from_tuple)  

# ## 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

# my_tuple = (5, 10, 3, 8, 2)

# max_value = max(my_tuple)
# min_value = min(my_tuple)

# print("Maximum:", max_value)
# print("Minimum:", min_value)


# ## 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

# my_words = ("apple", "banana", "cherry", "pear", "strawberry")
# reversed_tuple = my_words[::-1]
# print(reversed_tuple)
