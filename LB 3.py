import numpy as np
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print("2D Array:")
print(matrix)
third_column = matrix[:, 2]
print("\nThird Column:")
print(third_column)

n = int(input("\nEnter the number of elements: "))

print("Enter the elements:")

arr = np.array([int(input()) for i in range(n)])

reverse = arr[::-1]

print("\nOriginal Array:")
print(arr)

print("Reversed Array:")
print(reverse)

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9, 10],
              [11, 12, 13, 14],
              [15, 16, 17, 18]])

result = np.matmul(A, B)

print("\nFirst Matrix (2x3):")
print(A)

print("\nSecond Matrix (3x4):")
print(B)

print("\nMatrix Multiplication:")
print(result)

print("\nEnter 9 elements for a 3x3 Matrix:")

det_matrix = np.array([int(input()) for i in range(9)]).reshape(3, 3)

det = np.linalg.det(det_matrix)

print("\nMatrix:")
print(det_matrix)

print("\nDeterminant:")
print(det)