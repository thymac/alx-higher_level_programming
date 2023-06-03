#!/bin/bash
# A script that sends a DELETE request to the specified URL and displays the response

url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" -L "$url")

if [[ $response == "200" ]]; then
    body=$(curl -s -L "$url" -X DELETE)
    if [[ $? -eq 0 ]]; then
        echo "$body"
    else
        echo "Error: Failed to retrieve response body."
    fi
else
    echo "Error: Non-200 status code received - $response"
fi
