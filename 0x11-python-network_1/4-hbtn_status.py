#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''
import requests


if __name__ == "__main__":
    # Send a GET request to the URL using requests
    URL = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(URL)

    # Display the body of the response in the specified format
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
