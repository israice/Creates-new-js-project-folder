#!/usr/bin/env python3
import os
import re

# Settings
# Define the descriptive name for the new folder
FOLDER_NAME = 'NEW-FOLDER'
# Number of digits for the numeric prefix (e.g., 2 -> '01', 3 -> '001')
PREFIX_WIDTH = 2
# List of additional files to create in the base directory
ADDITIONAL_FILES = [
    'run.js',
    'README.md',
]
# List of core files to create inside the 'core' directory
CORE_FILES = [
    'index.html',
    'style.css',
    'script.js',
]

# Template content for README.md exactly as provided by the user
README_TEMPLATE = """# About
- https://github.com/XXXXXX/XXXXXXXXXXXXXXXXXX.git
- ABOUT THE PROJECT NAME
- ABOUT THE PROJECT

# DEV Log
## v001
- PROJECT CREATED DATE 2025.12.31 


# Github CHEATSHEET
## Create new repository
git init  
git add .  
git commit -m "COMMENT NAME"  
gh repo create  

## Load last updates and replace existing local files
git fetch origin; git reset --hard origin/master; git clean -fd  

## Select a hash from the last 10 commits
git log --oneline -n 10  

## Use the hash to get that exact version locally
git fetch origin; git checkout master; git reset --hard 1eaef8b; git clean -fdx  

## Update repository
git add .  
git commit -m "COMMENT NAME"  
git push
"""

def get_next_prefix_number():
    """
    Scan the current directory for folders with numeric prefixes and return the
    smallest positive integer not yet used.
    """
    entries = os.listdir('.')
    prefix_numbers = []
    for entry in entries:
        if os.path.isdir(entry):
            m = re.match(r'^(\d+)-', entry)
            if m:
                try:
                    prefix_numbers.append(int(m.group(1)))
                except ValueError:
                    continue
    # Find the smallest positive integer not in the existing prefixes
    n = 1
    existing = set(prefix_numbers)
    while n in existing:
        n += 1
    return n

def create_project_structure():
    # Determine the next available prefix number
    next_num = get_next_prefix_number()
    prefix = f"{next_num:0{PREFIX_WIDTH}d}"
    base_dir = f"{prefix}-{FOLDER_NAME}"

    # Create the base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create additional files in the base directory
    for filename in ADDITIONAL_FILES:
        file_path = os.path.join(base_dir, filename)
        if filename == 'README.md':
            # Write the exact README content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(README_TEMPLATE)
        else:
            # Create an empty file for other filenames
            open(file_path, 'w').close()

    # Create the 'core' directory inside the base directory
    core_dir = os.path.join(base_dir, 'core')
    os.makedirs(core_dir, exist_ok=True)

    # Create core files inside the 'core' directory
    for filename in CORE_FILES:
        open(os.path.join(core_dir, filename), 'w').close()

    print(f'Project structure created successfully in "{base_dir}".')

if __name__ == '__main__':
    create_project_structure()
