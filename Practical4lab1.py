import numpy as np

# a) 4x4 Identity Matrix
identity = np.eye(4)
print("4x4 Identity Matrix:")
print(identity)

# b) Two 3x3 random matrices
A = np.random.randint(1, 10, (3,3))
B = np.random.randint(1, 10, (3,3))

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
add = A + B
print("\nMatrix Addition:")
print(add)

# Matrix Multiplication
mul = np.dot(A, B)
print("\nMatrix Multiplication:")
print(mul)