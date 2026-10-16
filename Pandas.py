import pandas as pd

# 1. Create a Series
s = pd.Series([10, 20, 30, 40, 50])
print("Series:\n", s)

# 2. Create a DataFrame
data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "Raj"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# 3. Display first rows
print("\nFirst 2 rows:\n", df.head(2))

# 4. Display last rows
print("\nLast 2 rows:\n", df.tail(2))

# 5. Display column names
print("\nColumns:", df.columns)

# 6. Display shape
print("\nShape:", df.shape)

# 7. Display information
print("\nInformation:")
df.info()

# 8. Display statistical summary
print("\nStatistics:\n", df.describe())

# 9. Select a column
print("\nNames:\n", df["Name"])

# 10. Filter rows
print("\nStudents scoring above 85:\n", df[df["Marks"] > 85])

# 11. Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]
print("\nAfter adding column:\n", df)

# 12. Update a value
df.loc[0, "Marks"] = 92
print("\nAfter updating marks:\n", df)

# 13. Sort by marks
print("\nSorted by marks:\n", df.sort_values("Marks"))

# 14. Calculate average marks
print("\nAverage Marks:", df["Marks"].mean())

# 15. Find maximum and minimum marks
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# 16. Count values
print("\nResult Counts:\n", df["Result"].value_counts())

# 17. Check missing values
print("\nMissing Values:\n", df.isnull().sum())