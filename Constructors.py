class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


s1 = Student("Tahir", 21, 85)
s2 = Student("Rahul", 20, 90)

s1.display()
print()
s2.display()