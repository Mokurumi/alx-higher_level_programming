#!/usr/bin/python3
'''
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.
'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./6-post_email.py <URL> <email>")

    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent in the POST request
    data = {'email': email}

    # Send a POST request to the provided URL with the email parameter
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
