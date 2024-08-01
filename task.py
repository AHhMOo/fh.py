import os

def list_directory_contents(path):
    try:
        if not os.path.exists(path):
            print(f"The path '{path}' does not exist.")
            return
        if not os.path.isdir(path):
            print(f"The path '{path}' is not a directory.")
            return
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
    except PermissionError:
        print(f"Permission denied: Unable to access '{path}'")
    except Exception as e:
        print(f"An error occurred: {e}")
path = input("Enter the directory path to list its contents: ")
list_directory_contents(path)
