#!/bin/bash
# A script sends a GET request with a custom header, displays the response body
curl -s $1 -H "X-School-User-Id: 98"

