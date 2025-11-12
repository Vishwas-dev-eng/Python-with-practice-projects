import os

# Specify the directory path
directory_path = '/' # Enter the path you want to list   . 

try:
    # List all entries in the specified directory
    entries = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access the directory '{directory_path}'.")
except OSError as error:
    print(f"Error: An OS error occurred: {error}")
