#!/bin/bash
# This script sends a GET request to a given URL and displays the body of a 200 status code response
curl -s -o temp_body.txt -w "%{http_code}" "$1" | grep -q "^200$" && cat temp_body.txt && rm temp_body.txt
