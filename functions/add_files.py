# Function to add files to the repo on a default branch
import os

def add_files_and_directories_to_repository(repo, directory_path, commit_message):
    try:
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as file:
                    content = file.read()

                relative_path = os.path.relpath(file_path, directory_path)
                repo.create_file(relative_path, commit_message, content)
                print(f"{relative_path} has been added to the repository with the message: {commit_message}")

    except Exception as e:
        print(f"An error occurred while adding files and directories from the directory: {str(e)}")
