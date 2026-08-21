# DICTIONARY OPERATIONS
student = {
    "name": "Tahir",
    "age": 21,
    "course": "CSE",
    "marks": 85
}

print("Original Dictionary:", student)

# 1. Access value
print("1. Name:", student["name"])

# 2. get()
print("2. Course:", student.get("course"))

# 3. Add new key-value pair
student["city"] = "Kolhapur"
print("3. After adding city:", student)

# 4. Update value
student["marks"] = 90
print("4. After updating marks:", student)

# 5. keys()
print("5. Keys:", student.keys())

# 6. values()
print("6. Values:", student.values())

# 7. items()
print("7. Items:", student.items())

# 8. pop()
student.pop("age")
print("8. After pop:", student)

# 9. Check key
print("9. Is 'name' present?", "name" in student)

# 10. Update dictionary
student.update({"year": "Second Year"})
print("10. After update:", student)