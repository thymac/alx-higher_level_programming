#!/bin/bash
# A script that takes a URL, sends a GET request, displays the response body
curl - sI "$1" | grep - i Content - Length | awk '{print $2}'
