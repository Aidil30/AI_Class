import numpy as np

# Define matrices A, B, and C
A = np.array([[2, 0, -3], [1, 4, 5]])
B = np.array([[3, 1], [-1, 0], [4, 2]])
C = np.array([[4, 7], [2, 1], [1, -1]])

# Calculate AB and AC
AB = np.dot(A, B)
AC = np.dot(A, C)

# Calculate AB + AC
result = AB + AC

print("AB:")
print(AB)
print("\nAC:")
print(AC)
print("\nAB + AC:")
print(result)


# Function to perform matrix multiplication
def matrix_multiply(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    
    for i in range(len(X)):             # Loop over rows of X
        for j in range(len(Y[0])):       # Loop over columns of Y
            for k in range(len(Y)):      # Loop over rows of Y / columns of X
                result[i][j] += X[i][k] * Y[k][j]
    return result

# Function to add two matrices
def matrix_add(X, Y):
    result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
    return result

# Define matrices A, B, and C
A = [
    [2, 0, -3],
    [1, 4, 5]
]
B = [
    [3, 1],
    [-1, 0],
    [4, 2]
]
C = [
    [4, 7],
    [2, 1],
    [1, -1]
]

# Perform matrix multiplications
AB = matrix_multiply(A, B)
AC = matrix_multiply(A, C)

# Add the two resulting matrices
result = matrix_add(AB, AC)

# Display results
print("AB:", AB)
print("AC:", AC)
print("AB + AC:", result)