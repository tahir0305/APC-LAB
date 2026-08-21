#Traverse an array
arr = [10, 20, 30, 40, 50]
for i in range(len(arr)):
    print(arr[i])

#Find sum and average of an array
arr = [10, 20, 30, 40, 50]
total = sum(arr)
average = total / len(arr)
print("Sum =", total)
print("Average =", average)

#Find the maximum and minimum elements in an array
arr = [10, 20, 30, 40, 50]
print("Maximum element:", max(arr))
print("Minimum element:", min(arr))

#Search for an element in an array
arr = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))
if key in arr:
    print("Element found")
else:
    print("Element not found")

#Reverse an array
arr = [10, 20, 30, 40, 50]
print(arr[::-1])

#Find common elements in two arrays
arr1 = [10, 20, 30, 40]
arr2 = [30, 40, 50, 60]
common = []
for num in arr1:
    if num in arr2:
        common.append(num)
print("Common elements:", common)

#Array module
from array import array
arr = array('i', [10, 20, 30, 40, 50])
print(arr)
arr.append(60)
print("After append:", arr)
arr.insert(2, 25)
print("After insert:", arr)
arr.remove(30)
print("After remove:", arr)