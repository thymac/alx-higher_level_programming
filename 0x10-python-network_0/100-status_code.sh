#!/bin/bash
# A script that sends a request to a URL and displays only the status codee
echo -n "$(curl -s -o /dev/null - w '%{http_code}' "$1")"
