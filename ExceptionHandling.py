# EXCEPTION HANDLING IN PYTHON

# 1. Basic try-except
print("1. Basic Exception Handling")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Enter valid integers.")


# 2. Multiple exceptions
print("\n2. Multiple Exceptions")

try:
    num = int(input("Enter a number: "))
    print("Number:", num)
    print("Result:", 100 / num)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)


# 3. try-except-else-finally
print("\n3. Else and Finally")

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
else:
    print("Result:", result)
finally:
    print("Execution completed.")


# 4. Raising an exception
print("\n4. Raise Exception")

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Eligible.")
except ValueError as e:
    print("Error:", e)


# 5. User-defined exception
print("\n5. User-Defined Exception")

class LowMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise LowMarksError("Marks must be between 0 and 100.")

    print("Valid marks:", marks)
except LowMarksError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Please enter an integer.")


# 6. Handling file errors
print("\n6. File Exception Handling")

try:
    file = open("student.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File does not exist.")