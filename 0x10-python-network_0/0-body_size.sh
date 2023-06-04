#!/bin/bash
# A script that takes a URL as an argument, sends a GET request to that URL
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
