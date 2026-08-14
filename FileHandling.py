#Creating a new file with x
file = open("student.txt","x")
file.write("Tahir\n")
file.write("Computer Science\n")
file.close()
print("File created and data written successfully.")

#Writing data to an existing file with w
file = open("student.txt","w")
file.write("Tahir\n")
file.write("Computer Science\n")
file.write("Age: 21\n")
file.close()
print("Data written to the file successfully.")

#Reading data from the file with r
file = open("student.txt", "r") 
data = file.read()
print(data)
file.close()

#Reading data from the file with readline
file = open("student.txt", "r")
line = file.readline()
print(line)
file.close()

#Reading data from the file with readlines
file = open("student.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
file.close()

#Appending data to the file with a
file = open("student.txt", "a")
file.write("GPA: 9.3\n")
file.close()
print("Data appended to the file successfully.")

#Write data to the file with writelines
file = open("student.txt", "w")
data = [
    "Name: Tahir\n",
    "Course: Computer Science\n",
    "Year: Second Year\n"
]
file.writelines(data)
file.close()
print("Data written to the file successfully.")

#Check if a file exists before creating it with x
try:
    file = open("student.txt", "x")
    file.write("Hello Python")
    file.close()
    print("File created.")
except FileExistsError:
    print("File already exists.")

#Read and write data to a file using with statement
with open("greeting.txt", "w") as file:
    file.write("Hello Python")
with open("greeting.txt", "r") as file:
    data = file.read()
    print(data)

#Binary file handling
with open("data.bin", "wb") as file:
    data = b"Hello Python"
    file.write(data)
print("Binary file created successfully.")

#Renaming a file
import os
os.rename("greeting.txt", "new_greeting.txt")
print("File renamed successfully.")

#Check File position with tell() and seek()
file = open("student.txt", "r")
print(file.tell())
file.read(5)
print(file.tell())
file.close()

file = open("student.txt", "r")
print(file.read(5))
file.seek(0)
print(file.read())
file.close()

