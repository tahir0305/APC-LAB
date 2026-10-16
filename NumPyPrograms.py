import numpy as np

# 1. Check NumPy installation
print("NumPy Version:", np.__version__)

# 2. Create and print 1D array
a = np.array([10, 20, 30, 40])
print("\n1D Array:")
print(a)

# 3. Create and print 2D array
b = np.array([[10, 20], [30, 40]])
print("\n2D Array:")
print(b)

# 4. Create and print 3D array
c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("\n3D Array:")
print(c)

# 5. Create two 2D arrays for arithmetic operations
A = np.array([[10, 20], [30, 40]])
B = np.array([[2, 4], [5, 8]])

print("\nArray A:\n", A)
print("Array B:\n", B)

# 6. Addition
print("\nAddition:\n", np.add(A, B))

# 7. Subtraction
print("\nSubtraction:\n", np.subtract(A, B))

# 8. Multiplication (element-wise)
print("\nMultiplication:\n", np.multiply(A, B))

# 9. Division (element-wise)
print("\nDivision:\n", np.divide(A, B))

# 10. Transpose
print("\nTranspose of A:\n", np.transpose(A))

# 11. Exponential
print("\nExponential of A:\n", np.exp(A))

# 12. Add character labels to array
labels = np.array(["A", "B", "C", "D"])
values = np.array([10, 20, 30, 40])

print("\nCharacter Labels:")
for label, value in zip(labels, values):
    print(label, ":", value)

# 13. Display array dimensions and shape
print("\nDimensions:")
print("1D:", a.ndim)
print("2D:", b.ndim)
print("3D:", c.ndim)

print("\nShape of 2D array:", b.shape)