# Codes for patterns
for i in range(3):
    for j in range(65, 68):
        print(chr(j), end=" ")
    print()

n=int(input("Enter a number(n): "))

for i in range(1, n+1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()
print(end="\n")
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()
print(end="\n")
for i in range(1, n+1):
    for j in range(i):
        print(j+1, end=" ")
    print()
print(end="\n")
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()