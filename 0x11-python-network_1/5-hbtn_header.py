#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL,
and displays the value of the variable X-Request-Id in the response header
'''
import requests
import sys


if __name__ == "__main__":
    # Check if a URL argument is provided
    if len(sys.argv) < 2:
        print("Usage: 5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Send a GET request to the provided URL
    response = requests.get(url)

    # Check if the 'X-Request-Id' header exists in the response
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
