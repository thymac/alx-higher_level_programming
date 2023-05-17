#!/bin/bash
# A script to send a GET request to a URL and display the body of the response

URL=$1
curl -s -L "$URL"
