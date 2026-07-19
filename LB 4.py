import numpy as np
arr = np.random.randint(1, 100, (3, 4))
print("Random 2D Array:")
print(arr)

print("\nMean of Rows (Axis=1):")
print(np.mean(arr, axis=1))

print("\nMean of Columns (Axis=0):")
print(np.mean(arr, axis=0))

n = int(input("\nEnter number of elements: "))

print("Enter the elements:")

array = np.array([int(input()) for i in range(n)])

print("\nArray:")
print(array)

print("Minimum Value:", np.min(array))
print("Maximum Value:", np.max(array))

size = int(input("\nEnter size of the array: "))

print("Enter the elements:")

arr1 = np.array([int(input()) for i in range(size)])

constant = int(input("Enter the constant value: "))

result = arr1 + constant

print("\nOriginal Array:")
print(arr1)

print("Array after Adding Constant:")
print(result)

rows = int(input("\nEnter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix elements:")

matrix = np.array([[int(input()) for j in range(cols)] for i in range(rows)])

print("\nEnter", rows, "constants (one for each row):")

constants = np.array([int(input()) for i in range(rows)])

result = matrix * constants.reshape(rows, 1)
print("\nOriginal Matrix:")
print(matrix)
print("\nConstants:")
print(constants)
print("\nMatrix after Row-wise Multiplication:")
print(result)