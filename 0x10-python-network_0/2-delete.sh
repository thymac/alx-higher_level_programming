#!/bin/bash
# A script that sends a DELETE request to the specified URL and displays the response

curl -s "$1" -X DELETE
