import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Student Registration")
root.geometry("350x300")

# Heading
tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 14, "bold")
).pack(pady=10)

# Name
tk.Label(root, text="Enter Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Roll number
tk.Label(root, text="Enter Roll Number:").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

# Course
tk.Label(root, text="Enter Course:").pack()
course_entry = tk.Entry(root)
course_entry.pack()


# Submit function
def submit():
    name = name_entry.get().strip()
    roll = roll_entry.get().strip()
    course = course_entry.get().strip()

    if not name or not roll or not course:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        messagebox.showinfo(
            "Registration Successful",
            f"Name: {name}\nRoll Number: {roll}\nCourse: {course}"
        )


# Buttons
tk.Button(root, text="Submit", command=submit).pack(pady=10)
tk.Button(root, text="Clear", command=lambda: [
    name_entry.delete(0, tk.END),
    roll_entry.delete(0, tk.END),
    course_entry.delete(0, tk.END)
]).pack()

# Run application
root.mainloop()