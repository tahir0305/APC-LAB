import re

text = "Python is easy. Python is powerful. My number is 9876543210."

# 1. match() - checks the beginning
print("1. Match:")
result = re.match("Python", text)
print(result.group() if result else "No match")


# 2. search() - finds the first match
print("\n2. Search:")
result = re.search("easy", text)
print(result.group() if result else "Not found")


# 3. findall() - finds all matches
print("\n3. Find All:")
print(re.findall("Python", text))


# 4. find digits
print("\n4. Extract Digits:")
print(re.findall(r"\d", text))


# 5. Find all numbers
print("\n5. Find Numbers:")
print(re.findall(r"\d+", text))


# 6. sub() - replace text
print("\n6. Replace:")
print(re.sub("Python", "Java", text))


# 7. split() - split using a pattern
print("\n7. Split:")
print(re.split(r"\s+", "Python is easy to learn"))


# 8. Character classes
print("\n8. Character Classes:")
sample = "Python123!"
print("Letters:", re.findall(r"[a-zA-Z]", sample))
print("Digits:", re.findall(r"[0-9]", sample))
print("Non-alphanumeric:", re.findall(r"[^a-zA-Z0-9]", sample))


# 9. Validate email
print("\n9. Email Validation:")
email = input("Enter email: ")

if re.fullmatch(r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}", email):
    print("Valid email format")
else:
    print("Invalid email format")


# 10. Validate 10-digit phone number
print("\n10. Phone Validation:")
phone = input("Enter 10-digit phone number: ")

if re.fullmatch(r"[0-9]{10}", phone):
    print("Valid phone format")
else:
    print("Invalid phone format")


# 11. Quantifiers
print("\n11. Quantifiers:")
data = "a aa aaa aaaa"
print("Two or more a's:", re.findall(r"a{2,}", data))


# 12. Find words starting with P
print("\n12. Words Starting with P:")
sentence = "Python Programming is Pretty Powerful"
print(re.findall(r"\bP\w*", sentence))