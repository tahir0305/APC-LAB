import FileHandling
import Directories

# Directory Handling
Directories.current_directory()
Directories.create_directory("my_folder")
Directories.check_directory("my_folder")
Directories.list_directory("my_folder")

# File Handling
filename = "my_folder/student.txt"
FileHandling.create_file(filename)
FileHandling.write_file(filename)
FileHandling.append_file(filename)
FileHandling.read_file(filename)

# Binary File Handling
FileHandling.binary_file("my_folder/data.bin") 