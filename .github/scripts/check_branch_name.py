import re
import os
import json

# Function to get branch name
def get_branch_name():
    # Load the GitHub event data from the event path
    event_path = os.getenv('GITHUB_EVENT_PATH')
    with open(event_path) as f:
        event_data = json.load(f)

    # Get the branch name from the pull request data
    return event_data['pull_request']['head']['ref']

# Check branch name against pattern
branch_name = get_branch_name()
pattern = re.compile(r'^feature/\d+$')

if not pattern.match(branch_name):
    message = f'Branch name "{branch_name}" does not match the pattern "feature/<number>".'
    raise ValueError(message)