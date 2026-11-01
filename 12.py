from asyncio import streams
import os
from textwrap import indent


def list_directory_contents(path,inside=0):
    try:
        # List all items in the given path
        items = os.listdir(path)
    except PermissionError:
        print(" " * indent + f"[ACCESS DENIED]{path}")
        return
    for item in items:
        full_path = os.path.join(path,item)
        if os.path.isdir(full_path):
            print(" " * indent + f"[DIR]{item}")

# Run program
folder_path = input("Enter directory path:")
if os.path.exsists(folder_path)
    list_directory_contents(folder_path)
else:
    print("invalid path!")