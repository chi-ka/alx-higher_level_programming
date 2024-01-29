#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Construct the data to be sent in the POST request
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes

    # Make the POST request and read the response
    with urllib.request.urlopen(url, data) as response:
        response_text = response.read().decode('utf-8')
        print(response_text)
