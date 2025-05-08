# About
- https://github.com/israice/Creates-new-js-project-folder.git
- Creates new js project folder



# DEV Log
## v001
- create create_new_js_project.py 
- add README.md creation
- add data to README.md


# Github CHEATSHEET
## Create new repository
git init  
git add .  
git commit -m "create create_new_js_project.py"  
gh repo create  

## Load last updates and replace existing local files
git fetch origin; git reset --hard origin/master; git clean -fd  
## Select a hash from the last 10 commits
git log --oneline -n 10  
## Use the hash to get that exact version locally
git fetch origin; git checkout master; git reset --hard 1eaef8b; git clean -fdx  

## Update repository
git add .  
git commit -m "add data to README.md"  
git push
