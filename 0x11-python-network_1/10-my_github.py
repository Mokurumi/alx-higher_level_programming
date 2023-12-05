#!/usr/bin/python3
'''
Python script that uses the GitHub API to display your user id
'''
import requests
import sys


if __name__ == "__main__":
    # Get GitHub username and personal access token from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API endpoint to retrieve user information
    url = f'https://api.github.com/user'

    # Send GET request to GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(f"{user_id}")
    else:
        print("None")
