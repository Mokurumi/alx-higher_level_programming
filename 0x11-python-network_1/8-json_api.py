#!/usr/bin/python3
'''
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
import sys


if __name__ == "__main__":
    # Get the letter from the command line arguments
    # or set it as an empty string if no argument is given
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    # Data to be sent in the POST request
    data = {'q': q}

    # Send a POST request to the specified URL with the letter parameter
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        # Try to parse the response as JSON
        json_resp = response.json()

        # Check if the response JSON is properly formatted and not empty
        if json_resp and isinstance(json_resp, dict):
            print("[{}] {}".format(json_resp['id'], json_resp['name']))
        else:
            print("No result")

    except ValueError:
        # Handle the case where the response is not valid JSON
        print("Not a valid JSON")
