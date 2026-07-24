# Check if a number is non-zero or zero
n=int(input("Enter a number: "))
if n>0:
    print("Non Zero Number: ",n,end=" ")
else:
    print("The number is zero: ",n,end=" ")

num1=int(input("\nEnter a number: "))
num2=int(input("Enter another number: "))
print(end="\n")

# Check greater no between 2 nos
if num1>num2:
    print(num1,"is greater than",num2)
elif num1==num2:
    print("Both numbers are equal: ",num1)
else:
    print(num2,"is greater than",num1)


