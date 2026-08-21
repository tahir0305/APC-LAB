import math
import random
import datetime
import os
import statistics
import sys

print("===== MATH MODULE =====")

print("Square root:", math.sqrt(64))
print("Factorial:", math.factorial(5))
print("Pi:", math.pi)


print("\n===== RANDOM MODULE =====")

print("Random number:", random.randint(1, 100))

numbers = [10, 20, 30, 40, 50]
print("Random choice:", random.choice(numbers))


print("\n===== DATETIME MODULE =====")

print("Today's date:", datetime.date.today())
print("Current time:", datetime.datetime.now())


print("\n===== OS MODULE =====")

print("Current directory:", os.getcwd())
print("Directory contents:", os.listdir())


print("\n===== STATISTICS MODULE =====")

marks = [70, 80, 90, 60, 85]

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))


print("\n===== SYS MODULE =====")

print("Python version:", sys.version)
print("Platform:", sys.platform)