# About
- https://github.com/israice/Creates-new-js-project-folder.git
- Creates new js project folder



# DEV Log
## v001
- create create_new_JS_project.py 
- add README.md creation
- add data to README.md
- create_new_PY_project.py
- create copy_files.py



## Load last updates and replace existing local files
git fetch origin; git reset --hard origin/master; git clean -fd  
## Select a hash from the last 10 commits
git log --oneline -n 10  
## Use the hash to get that exact version locally
git fetch origin; git checkout master; git reset --hard 1eaef8b; git clean -fdx  

## Update repository
git add .  
git commit -m "create copy_files.py"  
git push
