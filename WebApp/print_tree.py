import os

def print_directory_tree(startpath, prefix=""):
    for item in os.listdir(startpath):
        path = os.path.join(startpath, item)
        if os.path.isdir(path):
            print(prefix + "|-- " + item + "/")
            print_directory_tree(path, prefix + "|   ")
        else:
            print(prefix + "|-- " + item)

print_directory_tree(".")