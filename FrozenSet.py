# FROZENSET OPERATIONS
A = frozenset([1, 2, 3, 4, 5])
B = frozenset([4, 5, 6, 7, 8])

print("Frozen Set A:", A)
print("Frozen Set B:", B)

# 1. Union
print("1. Union:", A.union(B))

# 2. Intersection
print("2. Intersection:", A.intersection(B))

# 3. Difference
print("3. Difference A-B:", A.difference(B))

# 4. Symmetric Difference
print("4. Symmetric Difference:", A.symmetric_difference(B))

# 5. Membership
print("5. Is 3 present?", 3 in A)

# 6. Subset
C = frozenset([1, 2])
print("6. Is C subset of A?", C.issubset(A))

# 7. Superset
print("7. Is A superset of C?", A.issuperset(C))

# 8. Disjoint
D = frozenset([10, 11])
print("8. Are A and D disjoint?", A.isdisjoint(D))

# 9. Length
print("9. Length of A:", len(A))

# 10. Convert to list
print("10. Frozen set converted to list:", list(A))