# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


# Child class
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):
        self.display_name()
        print("Roll Number:", self.roll_no)


s = Student("Tahir", 54)
s.display()