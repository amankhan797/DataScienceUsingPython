# Assignment 4
# Go to the below link for outputs on Google collab.
# https://colab.research.google.com/drive/1tBeIkmqkPZ7E4uky0JMAtdQyh_HUJk9t?usp=sharing

# First we need to import essential libraris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix

# Q1. Draw heatmap of mango and apple
actual = ['apple','mango','apple','mango','apple','mango','apple','mango']
pred = ['apple','apple','apple','apple','mango','mango','apple','mango']
cm = confusion_matrix(actual,pred)
print(cm)
sn.heatmap(cm)
_______________________________________________

# Q2. Indexing and slicing program (numpy)
arr = np.array([1, 2, 3, 4, 5])
# Access a specific element
element = arr[2]  # Retrieves the element at index 2 (3rd element)
print(element)
_______________________________________________

# Q3. Vectorization program (numpy)
subset = arr[1:4]  # Retrieves elements from index 1 to 3
print(subset)
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
#addition
result= a + b
print(result)
#subtraction
result = a - b
print(result)
#multiplication
result = a * b
print(result)
#square
result = a ** b
print(result)
#division
result = a / b
print(result)
_______________________________________________

# Q4. Swapaxes() program (numpy)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
# Swap axes 0 and 1
swapped_matrix = matrix.swapaxes(0, 1)

print("Original Matrix:")
print(matrix)

print("\nSwapped Matrix:")
print(swapped_matrix)
_______________________________________________

# Q5. Tranpose() program(numpy)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# Transpose the matrix
transposed_matrix = matrix.transpose()
print("Original Matrix:")
print(matrix)
print("\nTransposed Matrix:")
print(transposed_matrix)
_______________________________________________

# Q6. Write a NumPy program to reverse an array (the first element becomes the last).
original_array = np.array([1, 2, 3, 4, 5])
# Reverse the array
reversed_array = original_array[::-1]
print("Original Array:", original_array)
print("Reversed Array:", reversed_array)
_______________________________________________

# Q7. Write a NumPy program to test element-wise for NaN of a given array.
myarray = np.array([1,np.nan,2,np.nan,3,np.nan])
# np.isnan(myarray)
a= myarray[np.logical_not(np.isnan(myarray))]
print(a)
_______________________________________________

# Q8. Write a NumPy program to find the number of elements in an array. It also finds the length of one array element in bytes and the total bytes consumed by the elements.
Myarray = np.array([[1,2,3,4,5,6,7,8,9]])
print("Array Size: ",Myarray.size)
print("Array Size in Bytes: ",Myarray.itemsize)
print("Total Bytes consumed by an element :",Myarray.size * Myarray.itemsize )
_______________________________________________

# Q9. Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array.
MYARRAY = np.array([[3, 5, 2], [8, 1, 9], [4, 7, 6]])
max= np.argmax(MYARRAY, axis=1)
min= np.argmin(MYARRAY, axis=0)
print("Indices of maximum values along each row:", max)
print("Indices of minimum values along each column:", min)
_______________________________________________

# Q10. Write a NumPy program to create an array of integers from 30 to 70.
array_hai_ye = np.arange(30,71)
print(array_hai_ye)
_______________________________________________

# Q11. Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
null_vector = np.zeros(10)
null_vector[5] = 11
print(null_vector)