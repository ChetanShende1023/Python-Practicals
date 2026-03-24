"""
Lab Assignment-2
Question: Develop an application using file handling to copy the contents 
of python script into another without including the comments. 
Ask the user about the source and destination file names. 
Print the content of both the files.
"""

import os

def copy_without_comments():
    # Ask the user for file names
    source = input("Enter the source Python file name (e.g., myscript.py): ")
    destination = input("Enter the destination file name (e.g., clean_script.py): ")

    if not os.path.exists(source):
        print(f"Error: Source file '{source}' does not exist.")
        return

    # 1. Process and copy content excluding comments
    with open(source, 'r') as src_file, open(destination, 'w') as dest_file:
        for line in src_file:
            # Skip lines that start with '#' (ignoring leading spaces)
            if not line.strip().startswith('#'):
                dest_file.write(line)

    # 2. Print content of the Source File
    print("\n" + "="*30)
    print(f"CONTENT OF SOURCE FILE: {source}")
    print("="*30)
    with open(source, 'r') as src_file:
        print(src_file.read())

    # 3. Print content of the Destination File
    print("\n" + "="*30)
    print(f"CONTENT OF DESTINATION FILE: {destination}")
    print("="*30)
    with open(destination, 'r') as dest_file:
        print(dest_file.read())

if __name__ == "__main__":
    copy_without_comments()
