#!/usr/bin/python3
"""
Module: 0-hbtn_status
Fetches https://alx-intranet.hbtn.io/status and displays the response body.

"""

import urllib.request

def fetch_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status.
    
    Returns:
        A string representing the response body.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()

    return body.decode('utf-8')


if __name__ == "__main__":
    """
    If this module is executed directly, fetches and displays the status.
    """
    print("Body response:")
    print("\t- type:", type(fetch_status()))
    print("\t- content:", fetch_status())
    print("\t- utf8 content:", fetch_status())

