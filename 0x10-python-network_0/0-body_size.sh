#!/bin/bash
# A script that takes a URL as an argument, sends a GET request to that URL, and displays the response body

curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
