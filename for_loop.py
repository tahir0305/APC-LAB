n=int(input("Enter a number: "))

#Numbers from 1 to n
for i in range(1, n+1):
    print(i, end=" ")

#Even numbers upto n
for i in range(2, n+1, 2):
    print(i, end=" ")

#Odd numbers upto n
for i in range(1, n+1, 2):
    print(i, end=" ")

#Series 1 2 4 6 n^2
num = 1
for i in range(n):
    print(num, end=" ")
    num = num * 2

