# Function which download files from the specific repository
import os

def download_files_from_github_repo(repo, files_to_download, output_dir):
    # Make sure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in files_to_download:
        try:
            # Get the file content using PyGithub
            contents = repo.get_contents(file)

            # Save the content to the output directory
            file_content = contents.decoded_content.decode("utf-8")
            file_path = os.path.join(output_dir, file)

            with open(file_path, "w") as f:
                f.write(file_content)
            print(f"Downloaded {file} and saved it to {file_path}")
        except Exception as e:
            print(f"Failed to download {file}: {str(e)}")