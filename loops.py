num=(int(input("Enter a number: ")))
#for loop to print numbers from 1 to num
for i in range(1,num+1):
    print(i)

#while loop to check if the number is even or odd
while num%2==0:
    print("Even")
    break
else:
    print("Odd")

#for-else loop to print numbers from num to 1
for i in range(num,0,-1):
    print(i)

else:
    print("Loop finished")    