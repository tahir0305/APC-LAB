import os

def current_directory():
    print("Current Directory:")
    print(os.getcwd())

def create_directory(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print("Directory created successfully.")
    else:
        print("Directory already exists.")

def list_directory(dirname):
    print("\nDirectory Contents:")
    print(os.listdir(dirname))

def check_directory(dirname):
    if os.path.isdir(dirname):
        print(dirname, "is a directory.")
    else:
        print(dirname, "is not a directory.")

def rename_directory(old_name, new_name):
    os.rename(old_name, new_name)
    print("Directory renamed successfully.")

def remove_directory(dirname):
    os.rmdir(dirname)
    print("Directory removed successfully.")