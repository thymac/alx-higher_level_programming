#!/bin/bash
# A script that sends a JSON POST request to a URL with the contents of a file in the body and displays the response

url=$1
filename=$2

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "File not found: $filename"
    exit 1
fi

# Read the file content into a variable
data=$(cat "$filename")

# Send the POST request with the JSON data and display the response body
response=$(curl -s -X POST -H "Content-Type: application/json" -d "$data" "$url")
echo -n "$response"
