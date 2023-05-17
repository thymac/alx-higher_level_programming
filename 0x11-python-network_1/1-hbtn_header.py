#!/usr/bin/python3
"""
Fetches a URL, sends a request, and displays the value of the X-Request-Id variable found in the response header.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)

