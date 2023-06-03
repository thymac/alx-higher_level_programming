#!/bin/bash
# A script to send a GET request to a URL and display the body of the response

url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" -L "$url")

if [[ $response == "200" ]]; then
    body=$(curl -s -L "$url")
    if [[ $? -eq 0 ]]; then
        echo "$body"
    else
        echo "Error: Failed to retrieve response body."
    fi
else
    echo "Error: Non-200 status code received - $response"
fi
