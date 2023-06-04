#!/bin/bash
# A script that displays all HTTP methods supported by the specified server

url =$1
response =$(curl - s - i - X OPTIONS "$url" | awk - F': ' '/Allow/ {print $2}')

if [[-n $response]]
then
echo "$response"
else
echo "Error: Failed to retrieve HTTP methods."
fi
