#1
# Lists to store student names and grades
students = []
grades = []

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    students.append(name)
    grades.append(grade)
    print("Student added successfully.\n")

# Function to update a student's grade
def update_grade():
    name = input("Enter student name to update: ")
    if name in students:
        index = students.index(name)
        grades[index] = float(input("Enter new grade: "))
        print("Grade updated successfully.\n")
    else:
        print("Student not found.\n")

# Function to remove a student
def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully.\n")
    else:
        print("Student not found.\n")

# Function to calculate average grade
def average_grade():
    if len(grades) > 0:
        avg = sum(grades) / len(grades)
        print("Average Grade =", avg)
    else:
        print("No student records available.")
    print()

# Function to display highest and lowest grades
def highest_lowest():
    if len(grades) > 0:
        print("Highest Grade =", max(grades))
        print("Lowest Grade =", min(grades))
    else:
        print("No student records available.")
    print()

# Function to display all students
def display_students():
    if len(students) > 0:
        print("\nStudent Records")
        for i in range(len(students)):
            print(students[i], ":", grades[i])
    else:
        print("No student records available.")
    print()


while True:
    print("===== Student Grade Management System =====")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest & Lowest Grade")
    print("6. Display All Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        update_grade()
    elif choice == 3:
        remove_student()
    elif choice == 4:
        average_grade()
    elif choice == 5:
        highest_lowest()
    elif choice == 6:
        display_students()
    elif choice == 7:
        print("Exiting Program...")
        break
    else:
        print("Invalid choice. Try again.\n")

#2
import math

# Function to calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Function to find the farthest point from the origin
def farthest_point(points):
    farthest = points[0]
    max_distance = math.sqrt(farthest[0]**2 + farthest[1]**2)

    for point in points:
        distance = math.sqrt(point[0]**2 + point[1]**2)
        if distance > max_distance:
            max_distance = distance
            farthest = point

    return farthest

# Main Program
n = int(input("Enter the number of points: "))

points = []

for i in range(n):
    x = float(input("Enter x-coordinate: "))
    y = float(input("Enter y-coordinate: "))
    points.append((x, y))

print("\nPoints:", points)

# Input two points for distance calculation
x1 = float(input("\nEnter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
point1 = (x1, y1)

x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))
point2 = (x2, y2)

distance = calculate_distance(point1, point2)
print("Distance between the two points =", distance)

# Find farthest point from origin
fp = farthest_point(points)
print("Farthest point from origin =", fp)


#3
# Server configuration
server_ip = ("192", "168", "1", "10")   # Tuple (cannot be changed)
allowed_ips = ["192.168.1.2", "192.168.1.3"]  # List (can be updated)

# Function to update allowed IPs
def update_allowed_ips():
    ip = input("Enter IP address to add: ")
    allowed_ips.append(ip)
    print("IP added successfully.\n")

# Function to display configuration
def display_configuration():
    print("Server IP:", ".".join(server_ip))
    print("Allowed IPs:", allowed_ips)
    print()

# Main Program
print("Current Configuration:")
display_configuration()

# Update allowed IPs
update_allowed_ips()

# Attempt to update server IP
print("Server IP cannot be modified because it is stored as a tuple.\n")

# Display updated configuration
print("Updated Configuration:")
display_configuration()


#4
# Input employees for Project 1
project1 = set(input("Enter employees of Project 1 (space-separated): ").split())

# Input employees for Project 2
project2 = set(input("Enter employees of Project 2 (space-separated): ").split())

# Employees working on both projects
common = project1.intersection(project2)

# Employees working only on Project 1
only_project1 = project1.difference(project2)

# Employees working only on Project 2
only_project2 = project2.difference(project1)

# Total unique employees
all_employees = project1.union(project2)

# Display results
print("\nEmployees working on both projects:", common)
print("Employees working only on Project 1:", only_project1)
print("Employees working only on Project 2:", only_project2)
print("Total unique employees:", all_employees)


#5
# Input paragraph
text = input("Enter a paragraph:\n")

# Convert to lowercase and split into words
words = text.lower().split()

# Count total words
total_words = len(words)

# Count frequency of each word
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Find top 3 most frequent words
sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1

# Display results
print("\nTotal number of words:", total_words)

print("\nWord Frequencies:")
for word, count in frequency.items():
    print(word, ":", count)

print("\nTop 3 Most Frequent Words:")
for word, count in sorted_words[:3]:
    print(word, ":", count)

print("\nTotal number of vowels:", vowel_count)