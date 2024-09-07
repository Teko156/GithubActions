# check_branch_name.py
import re
import os
import requests

# Function to get branch name
def get_branch_name():
    if os.getenv('GITHUB_EVENT_NAME') == 'pull_request':
        pr_number = os.getenv('GITHUB_REF').split('/')[-1]
        response = requests.get(f'https://api.github.com/repos/{os.getenv("GITHUB_REPOSITORY")}/pulls/{pr_number}',
                                headers={'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'})
        response.raise_for_status()
        pr_data = response.json()
        return pr_data['head']['ref']
    else:
        return os.getenv('GITHUB_REF').split('/')[-1]

# Check branch name against pattern
branch_name = get_branch_name()
pattern = re.compile(r'^feature/\d+$')

if not pattern.match(branch_name):
    message = f'Branch name "{branch_name}" does not match the pattern "feature/<number>".'
    raise ValueError(message)
