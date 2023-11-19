#!/usr/bin/env python3
import getpass # For securely inputting the PAT
import os
from github import Github
from functions import branch_protection
from functions import add_files
from functions import add_team
from functions import get_template_files

# Authenticate with a personal access token or OAuth token
pat = getpass.getpass('Enter your GitHub Personal Access Token: ')
g = Github(pat)

# Define the organization and new repository details
org_name = '<organization_name>'
repo_name = '<new_repository_name>'
repo_description = 'A new repository'
private = True

# This part will create the repository inside the organization
org = g.get_organization(org_name)
repo = org.create_repo(name=repo_name, description=repo_description, private=private)
print('Repository has been created ')

# Define which team should be added to the repository
team_name = '<team_name>'
add_team.add_team_to_repository(org, repo, team_name)

# Get files from starter repository for the newly created repository
source_repo_name = '<source_repository_name>'
source_repo = org.get_repo(name=source_repo_name)
files_to_download = ['.env.example', 'README.md', '.gitignore'] # example of files to get from starter repository
template_directory = 'template'
get_template_files.download_files_from_github_repo(source_repo, files_to_download, template_directory)

# Add files to the newly created repository
commit_message = 'Initial commit'
add_files.add_files_and_directories_to_repository(repo, template_directory, commit_message)

# Define to which branch you want to add protection rules
branch_name = 'develop'  # Change this to the branch you want to protect
branch_protection.add_branch_protection(org_name, repo_name, branch_name, pat)

# Clean template directory
# Iterate over the files in the list and delete them from the template directory
for filename in files_to_download:
    file_path = os.path.join(template_directory, filename)
    
    # Check if the file exists before attempting to delete it
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {filename}")
    else:
        print(f"{filename} not found")