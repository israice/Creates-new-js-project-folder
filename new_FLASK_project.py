#!/usr/bin/env python3
import os
import re

# Settings
# Define the descriptive name for the new folder
FOLDER_NAME = 'NEW-FOLDER'
# Number of digits for the numeric prefix (e.g., 2 -> '01', 3 -> '001')
PREFIX_WIDTH = 2
# Name of the core backend directory inside the base directory
CORE_BACKEND_DIR = os.path.join('core', 'BACKEND')

# Additional files in the base directory with minimal content
ADDITIONAL_FILES_CONTENTS = {
    '.env': """
PORT=5039
STATIC_FOLDER=core/FRONTEND
""",

    'requirements.txt': """
flask
requests
python-dotenv
""",

    'docker-compose.yaml': """
""",

    '.gitignore': """
""",

    'README.md': """
# About
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
""",

    'run.py': """
#!/usr/bin/env python3
import subprocess
import sys
import os
from dotenv import load_dotenv
from flask import Flask, send_from_directory

load_dotenv()

PORT = int(os.getenv('PORT'))
STATIC_FOLDER = os.getenv('STATIC_FOLDER')

static_path = os.path.abspath(STATIC_FOLDER)
app = Flask(__name__, static_folder=None)

@app.route('/')
def index():
    return send_from_directory(static_path, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(static_path, filename)

for script in ("core/BACKEND/A_run.py", "core/BACKEND/B_run.py"):
    code = subprocess.call([sys.executable, script])
    if code != 0:
        sys.exit(code)

if __name__ == '__main__':
    app.run(port=PORT)
""",

    'settings.yaml': """
""",
}

# Core backend files with minimal Python code
CORE_BACKEND_FILES = {
    'A_run.py': """
#!/usr/bin/env python3
import subprocess, sys

for script in (
    "core/BACKEND/test.py",
    ):
    if subprocess.call([sys.executable, script]) != 0:
        sys.exit(1)
""",

    'B_run.py': """
#!/usr/bin/env python3
import subprocess, sys

for script in (
    "core/BACKEND/test.py",
    ):
    if subprocess.call([sys.executable, script]) != 0:
        sys.exit(1)
""",

    'test.py': """
print('- - - ✅ Test')
""",
}

# Data files under core/DATA with minimal CSV headers
DATA_FILES = {
    'data_db.csv': """
""",

    'users_db.csv': """
""",
}

# Frontend files under core/FRONTEND with minimal boilerplate
FRONTEND_FILES = {
    'index.html': """
""",

    'script.js': """
""",

    'styles.css': """
""",
}

def get_next_prefix_number():
    """
    Scan the current directory for folders with numeric prefixes and return the
    smallest positive integer not yet used.
    """
    entries = os.listdir('.')
    nums = []
    for e in entries:
        if os.path.isdir(e):
            m = re.match(r'^(\d+)-', e)
            if m:
                try:
                    nums.append(int(m.group(1)))
                except ValueError:
                    pass
    n = 1
    used = set(nums)
    while n in used:
        n += 1
    return n

def create_project_structure():
    # Next prefix and base directory name
    num = get_next_prefix_number()
    prefix = f"{num:0{PREFIX_WIDTH}d}"
    base_dir = f"{prefix}-{FOLDER_NAME}"

    # Create base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create additional files
    for name, content in ADDITIONAL_FILES_CONTENTS.items():
        path = os.path.join(base_dir, name)
        # Ensure parent dirs exist (for .gitignore etc.)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    # Create core backend dir and files
    backend_dir = os.path.join(base_dir, CORE_BACKEND_DIR)
    os.makedirs(backend_dir, exist_ok=True)
    for name, content in CORE_BACKEND_FILES.items():
        with open(os.path.join(backend_dir, name), 'w', encoding='utf-8') as f:
            f.write(content)

    # Create DATA directory and CSV files
    data_dir = os.path.join(base_dir, 'core', 'DATA')
    os.makedirs(data_dir, exist_ok=True)
    for name, header in DATA_FILES.items():
        with open(os.path.join(data_dir, name), 'w', encoding='utf-8') as f:
            f.write(header)

    # Create FRONTEND directory and files
    fe_dir = os.path.join(base_dir, 'core', 'FRONTEND')
    os.makedirs(fe_dir, exist_ok=True)
    for name, content in FRONTEND_FILES.items():
        with open(os.path.join(fe_dir, name), 'w', encoding='utf-8') as f:
            f.write(content)

    print(f'- - - ✅ Project "{base_dir}" created successfully')

if __name__ == '__main__':
    create_project_structure()
