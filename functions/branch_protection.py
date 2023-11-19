# Function to add branch protection rules
# https://docs.github.com/en/rest/branches/branch-protection?apiVersion=2022-11-28#update-branch-protection

import requests

def add_branch_protection(organization_name, repository_name, branch_name, pat):
    # Define the branch protection rule data
    branch_protection_url = f"https://api.github.com/repos/{organization_name}/{repository_name}/branches/{branch_name}/protection"
    branch_protection_data = {
    "required_status_checks": {
        "strict": True,
        "checks": [
            {
                'context': 'pr-check-stage',
            }          
        ]  # Specific checks that are required to pass
    },
    "enforce_admins": True,
    "required_pull_request_reviews": {
        "dismiss_stale_reviews": True,
        "require_code_owner_reviews": False,
        "required_approving_review_count": 1,
        "require_last_push_approval": True,
    },
    "restrictions": None,
    "required_linear_history": False,
    "allow_force_pushes": False,
    "allow_deletions": False,
}

    # Set up the headers with the personal access token
    headers = {
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Make a PUT request to add branch protection
    response = requests.put(branch_protection_url, json=branch_protection_data, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print(f"Branch protection added to the '{branch_name}' branch of '{repository_name}'.")
    else:
        print(f"Failed to add branch protection. Status code: {response.status_code}")
        print(response.text)