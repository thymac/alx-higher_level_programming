#!/bin/bash
# send a request to an URL with curl and displays the size of the body of the response
URL="$1"
curl -s -w '%{size_download}' -o /dev/null "$URL"

