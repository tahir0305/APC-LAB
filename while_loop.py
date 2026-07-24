# Print natural numbers upto n and Sum
n=int(input("Enter a number: "))
i=1
sum=0
while i<=n:
    print(i,end=" ")
    sum+=i
    i+=1
print("Sum = ", sum)
print(end="\n")


# Print even numbers upto n and sum of Even nos
j=2
while j<=n:
    print(j,end=" ")
    sum+=j
    j+=2
print("Sum = ", sum)
print(end="\n")

# Print odd numbers upto n and sum of Odd nos
k=1
while k<=n:
    print(k,end=" ")
    sum+=k
    k+=2
print("Sum = ", sum)
print(end="\n")

# Print Factorial of n
fact=1
for l in range(1,n+1):
    fact*=l
print("Factorial of ",n," = ",fact)

print(end="\n")
# Print Fibonacci series upto n
a=0
b=1
while a<=n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c

print(end="\n")
#while loop to print multiplication table of num
num=(int(input("Enter a number: ")))
i=1
while i<11:
    print(num,"*",i,"=",num*i)
    i+=1