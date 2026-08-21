# SET OPERATIONS
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# 1. Add
A.add(10)
print("1. After add:", A)

# 2. Remove
A.remove(10)
print("2. After remove:", A)

# 3. Discard
A.discard(5)
print("3. After discard:", A)

# 4. Union
print("4. Union:", A.union(B))

# 5. Intersection
print("5. Intersection:", A.intersection(B))

# 6. Difference
print("6. Difference A-B:", A.difference(B))

# 7. Symmetric Difference
print("7. Symmetric Difference:", A.symmetric_difference(B))

# 8. Membership
print("8. Is 3 present?", 3 in A)

# 9. Subset
C = {1, 2}
print("9. Is C subset of A?", C.issubset(A))

# 10. Superset
print("10. Is A superset of C?", A.issuperset(C))