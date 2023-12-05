#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.
'''
import urllib.request
import sys


if __name__ == "__main__":
    # Check if a URL argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Send a request to the provided URL
    with urllib.request.urlopen(url) as response:
        # Check if the 'X-Request-Id' header exists in the response
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
