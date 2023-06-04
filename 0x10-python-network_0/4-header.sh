#!/bin/bash
# A script that sends a `GET` request to the specified URL with a custom
# header and displays the response

URL = "$1"
response =$(curl - s - H "X-School-User-Id: 98" "$URL")

if [[$? -eq 0]]
then
echo "$response"
else
echo "Error: Failed to retrieve response body."
fi
