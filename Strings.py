# Length of a string without using len() function
s = input("Enter a string : ")
count = 0
for ch in s:
    count += 1
print("The length of the string is:", count)

# Counting vowels, consonants, digits, spaces, and special characters in a string
st=input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0
for char in st:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_characters += 1 

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special_characters)

# Reverse a string without using built-in functions
n=input("Enter a string:")
reverse=""
for i in n:
    reverse=i+reverse
print("The reverse of the string is:",reverse)

# Check if a string is a palindrome
f=input("Enter a string:")
if f==f[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Uppercase and Lowercase count in a string
string=input("Enter a string:")
upper=0
lower=0
for chr in string:
    if chr.isupper():
        upper+=1
    elif chr.islower():
        lower+=1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

# Remove spaces from a string
string_with_spaces=input("Enter a string with spaces:")

r=""
for j in string_with_spaces:
    if j!=" ":
        r+=j
print("String after removing sapces:",r)

# Frequency of a specified character in a string
strng=input("Enter a string:")
chartr=input("Enter a character to search:")
cnt=0
for k in strng:
    if k==chartr:
        cnt+=1
print("The frequency of the character",chartr,"in the string is:",cnt)

# First and Last character of a string
str1=input("Enter a string:")
print("First character:",str1[0])
print("Last charcter:",str1[-1])

# Replace a character with another character in a string
str2=input("Enter a string:")
old_char=input("Enter the character to be replaced:")
new_char=input("Enter the new character:")
new_str=""
for l in str2:
    if l==old_char:
        new_str+=new_char
    else:
        new_str+=l
print("String after replacing the character:",new_str)