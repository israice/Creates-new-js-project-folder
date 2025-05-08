import os
import shutil

# Get the current directory
current_dir = os.path.abspath(os.getcwd())

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# List of files to copy
files_to_copy = [
    'create_new_JS_project.py', 
    'create_new_PY_project.py',
]

for filename in files_to_copy:
    src_path = os.path.join(current_dir, filename)
    dest_path = os.path.join(parent_dir, filename)
    
    if os.path.exists(src_path):
        # Copy the file and overwrite if it already exists
        shutil.copy2(src_path, dest_path)
        print(f"File {filename} successfully copied to {parent_dir}")
    else:
        print(f"File {filename} not found in {current_dir}")
