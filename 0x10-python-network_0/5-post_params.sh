#!/bin/bash
# A script that sends a `POST` request to the specified URL with the given parameters and displays the response

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"
response=$(curl -s -X POST -d "email=$email" -d "subject=$subject" "$url")

if [[ $? -eq 0 ]]; then
    echo "POST params:"
    echo "    email: $email"
    echo "    subject: $subject"
else
    echo "Error: Failed to retrieve response body."
fi
