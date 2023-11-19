# Function to add team to the repository

def add_team_to_repository(org, repo, team_name):
    try:
        team = None
        for org_team in org.get_teams():
            if org_team.name == team_name:
                team = org_team
                break

        if team:
            # Add the team to the repository with the specified permission
            # https://stackoverflow.com/questions/69329795/update-team-repositoryrepo-permission-not-updating-the-repo-permissions-in-gi
            # https://pygithub.readthedocs.io/en/latest/github_objects/Team.html?highlight=team%20add_to_repos#github.Team.Team.update_team_repository
            team.add_to_repos(repo=repo) # adds read permission for team on the repo
            team.update_team_repository(repo=repo, permission="push") # upgrade to write permissions
            print(f"Team with the name '{team_name}' added to the newly created repository")
        else:
            print(f"No team with the name '{team_name}' was found in the organization")

    except Exception as e:
        print(f"An error occurred while adding the team to the repository: {str(e)}")
