#!/bin/bash
# A script that sends a `POST` request to the specified URL with the given parameters and displays the response

curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
