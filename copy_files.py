import os
import shutil

current_dir = os.path.abspath(os.getcwd())
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

files_to_copy = [
    'new_JS_project.py',
    'new_FLASK_project.py',
    'new_CHROME_project.py',
]

for filename in files_to_copy:
    src_path = os.path.join(current_dir, filename)
    dest_path = os.path.join(parent_dir, filename)
    
    if os.path.exists(src_path):
        # Copy the file and overwrite if it already exists
        shutil.copy2(src_path, dest_path)

print(f"- - - ✅ Files copied to {parent_dir}")