#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions.
'''
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    # Check if a URL argument is provided
    if len(sys.argv) < 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send a request to the provided URL
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)

    except urllib.error.HTTPError as e:
        # Handle HTTPError exceptions
        print(f"Error code: {e.code}")
