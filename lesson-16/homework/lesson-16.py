# # 1. Convert List to 1D Array

# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# Expected Output:

# Original List: [12.23, 13.32, 100, 36.32]
# One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]

# import numpy as np

# my_ls = [12.23, 13.32, 100, 36.32]
# new_ls = np.array(my_ls)
# print(new_ls)

# # 2. Create 3x3 Matrix (2?10)

# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# Expected Output:

# [[ 2 3 4]
# [ 5 6 7]
# [ 8 9 10]]

# import numpy as np
# matrix = np.array([[2,3,4], [5,6,7], [8,9,10]])
# print(matrix)


# # 3. Null Vector (10) & Update Sixth Value

# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Update sixth value to 11
# [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

# import numpy as np
# vec = np.zeros(10)  
# vec[5] = 11 
# print(vec)


# # 4. Array from 12 to 38

# Write a NumPy program to create an array with values ranging from 12 to 38.

# Expected Output:

# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

# import numpy as np
# array = np.arange(12,39)
# print(array)


# # 5. Convert Array to Float Type

# Write a NumPy program to convert an array to a floating type.

# Sample output:

# Original array
# [1, 2, 3, 4]

# import numpy as np
# orig = np.array([1, 2, 3, 4])
# float_arr = orig.astype(float)
# print(float_arr)

# # 6. Celsius to Fahrenheit Conversion

# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. 
# Centigrade values are stored in a NumPy array.

# Sample Array [0, 12, 45.21, 34, 99.91]
# [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

# Expected Output:

# Values in Fahrenheit degrees:
# [ 0. 12. 45.21 34. 99.91 32. ]

# Values in Centigrade degrees:
# [-17.78 -11.11 7.34 1.11 37.73 0. ]

# Values in Centigrade degrees:
# [-17.78 -11.11 7.34 1.11 37.73 0. ]

# Values in Fahrenheit degrees:
# [-0. 12. 45.21 34. 99.91 32. ]

# import numpy as np
# celsius = np.array([0, 12, 45.21, 34, 99.91])
# fahrenheit = (celsius * 9/5) + 32
# print("Fahrenheit:", fahrenheit)
# print("Celsius:", celsius)

# # 7. Append Values to Array (Do self-tudy)

# Write a NumPy program to append values to the end of an array.

# Expected Output:

# Original array:
# [10, 20, 30]

# After append values to the end of the array:
# [10 20 30 40 50 60 70 80 90]

# import numpy as np
# arr = np.array([10, 20, 30])
# arr = np.append(arr, [40, 50, 60, 70, 80, 90])
# print(arr)


# # 8. Array Statistical Functions (Do self-tudy)

# Create a random NumPy array of 10 elements and calculate the mean, median, and 
# standard deviation of the array.


# import numpy as np

# arr = np.random.rand(10)  # 10 случайных чисел от 0 до 1
# print("Mean:", arr.min())
# print("Median:", np.median(arr))
# print("Std:", arr.std())

# # 9 Find min and max 

# Create a 10x10 array with random values and find the minimum and maximum values.

# import numpy as np

# arr = np.random.rand(10,10)  # 10 случайных чисел от 0 до 1
# print("Min:", np.min(arr))
# print("Max:", np.max(arr))



# # 10 

# Create a 3x3x3 array with random values.

# import numpy as np

# arr = np.random.rand(3, 3, 3)
# print(arr)