#!/bin/bash
# A script that takes a URL as an argument, sends a GET request to that URL, and displays the response body
URL="$1"
curl -sI "$URL" | grep -i Content-Length | awk '{print $2}'
