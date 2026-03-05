import numpy as np

# Input for 5x3 matrix
print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input().split()))
    A.append(row)

# Input for 3x2 matrix
print("Enter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

# Matrix multiplication
C = np.dot(A, B)

print("Product Matrix:")
print(C)