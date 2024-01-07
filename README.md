# Python project for initial setup of a repository for some project  

This project should automate the initial setup of a repository for some project  

## Getting Started

1. Clone the repository `git clone`
2. Make sure that you have installed *python3* on your machine
3. Make sure that you have installed *pip* on your machine
4. Install dependencies `pip3 install PyGithub`

## Usage

1. Set desired variables in the *main.py* file
2. Run the *main.py* script `python3 main.py`

The main script will prompt us for the Personal Access Token to authenticate us with GitHub. After that, the script will create a repository named after the *repo_name* variable. Then it will add the desired team (*team_name*) to the newly created repository with the *Write* permission. Finally, it will add necessary files from the starter repository (*some-starter*) and a branch protection rule to the *develop* branch. The branch protection rule should make us commit to the *develop* branch only through PR, with a colleague's approval, and only if all checks are successful.
