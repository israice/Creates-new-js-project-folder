# About
- https://github.com/israice/Creates-new-js-project-folder.git
- Creates new project folder for 
    - Python
    - JavaScript 
    - Chrome Extention 

# DEV Log
## v001
- create create_new_JS_project.py 
- add README.md creation
- add data to README.md
- create_new_PY_project.py
- create copy_files.py
## v002
- create_new_CHROME_project.py
- added .env to projects
## v003
- added flask completed start with html css js



## Load last updates and replace existing local files
git fetch origin; git reset --hard origin/master; git clean -fd  
## Select a hash from the last 10 commits
git log --oneline -n 10  
## Use the hash to get that exact version locally
git fetch origin; git checkout master; git reset --hard 1eaef8b; git clean -fdx  

## Update repository
git add .  
git commit -m "added flask completed start with html css js"  
git push
