#!/bin/bash
# A script that sends a JSON POST request to a URL with the contents of a file in the body and displays the response

curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
