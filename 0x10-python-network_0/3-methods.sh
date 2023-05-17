#!/bin/bash
# A script that displays all HTTP methods supported by the specified server

curl -sI "$1" | grep -i Allow | cut -d' ' -f2-
