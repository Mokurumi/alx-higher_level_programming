#!/usr/bin/python3
'''
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    # Check if enough arguments (URL and email) are provided
    if len(sys.argv) < 3:
        print("Usage: /2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode()

    # Send a POST request to the provided URL with the email parameter
    with urllib.request.urlopen(url, data=data) as response:
        html = response.read().decode('utf-8')
        print(html)
