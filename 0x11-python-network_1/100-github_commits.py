#!/usr/bin/python3
'''
Python script that lists 10 commits (from the most recent to oldest)
of a repository by a specified owner using the GitHub API.
'''
import requests
import sys


if __name__ == "__main__":
    # Get repository name and owner name from command line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API endpoint to retrieve commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Parameters to get the most recent 10 commits
    params = {'per_page': 10}

    # Send GET request to GitHub API to retrieve commits
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        commits = response.json()

        # Loop through each commit and print commit information
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Failed to retrieve commits. Check the repo and owner names.")
