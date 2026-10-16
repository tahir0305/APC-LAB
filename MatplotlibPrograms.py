import matplotlib.pyplot as plt

# Sample data
subjects = ["Python", "Java", "C++", "DBMS", "OS"]
marks = [85, 90, 78, 95, 88]

# 1. Line Plot
plt.figure()
plt.plot(subjects, marks, marker="o")
plt.title("Line Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# 2. Bar Chart
plt.figure()
plt.bar(subjects, marks)
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 3. Horizontal Bar Chart
plt.figure()
plt.barh(subjects, marks)
plt.title("Horizontal Bar Chart")
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.show()

# 4. Scatter Plot
plt.figure()
plt.scatter(subjects, marks)
plt.title("Scatter Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 5. Histogram
plt.figure()
plt.hist(marks, bins=5)
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 6. Pie Chart
plt.figure()
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()

# 7. Subplot: two graphs in one figure
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(subjects, marks, marker="o")
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(subjects, marks)
plt.title("Bar Chart")

plt.tight_layout()
plt.show()

# 8. Save a graph
plt.figure()
plt.plot(subjects, marks, marker="o")
plt.title("Saved Marks Graph")
plt.savefig("marks_graph.png")
plt.show()