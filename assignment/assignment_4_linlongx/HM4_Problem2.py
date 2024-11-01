import os

def walk_directory(path, indent=""):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            print(f"{indent}{entry}/")
            walk_directory(full_path, indent + "  ")
        else:
            print(f"{indent}{entry}")

# Main
dir_path = input("Enter directory path to walk through: ")
walk_directory(dir_path)
