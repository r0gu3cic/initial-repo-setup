# Python project for initial setup of a repository for the React projects  

This project should automate the initial setup of a repository for a new React project following the best practices developed by our team  

## Getting Started

1. Clone the repository `git clone`
2. Make sure that you have installed *python3* on you machine
3. Make sure that you have installed *pip* on you machine
4. Install dependencies `pip3 install PyGithub`

## Usage

1. Set desired variables in the *main.py* file
2. Run the *main.py* script `python3 main.py`

The main script will prompt us for the Personal Access Token to authenticate us with the GitHub. After that script will create a repository named after the *repo_name* variable. Then it will add desired team (*team_name*) to the newly created repository with the *Write* permission. Finally it will add necessary files from the starter repository (*reactjs-starter*) and it will add branch protection rule to the *develop* branch. The branch protection rule should make us commit to the *develop* branch only through PR, with the approve of a colleague and only if all checks are successful.

**What needs to be done?**  

- ~~Create a repo~~  
- ~~Add README.md file~~  
- ~~Add Pull Request file~~  
- ~~Add .gitignore file~~  
- ~~Add formatting rules file (.prettierrc)~~  
- ~~Add linting rules file (.eslintrc.json)~~  
- ~~Add build check and lint check as a GitHub Actions workflow~~  
- ~~Add branch protecting rules to the repo (Only merge through PR and checks need to pass)~~  
- ~~Add team to the repo~~  
- ~~Pull files from reactjs-starter repo~~  
- ~~Clear template directory for next usage~~
