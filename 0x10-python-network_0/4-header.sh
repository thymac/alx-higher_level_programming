#!/bin/bash
# A script that sends a `GET` request to the specified URL with a custom header and displays the response
URL="$1"
curl -s -H "X-School-User-Id: 98" "$URL"
