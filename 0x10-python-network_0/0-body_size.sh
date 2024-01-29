#!/bin/bash
# This script takes a URL as input and outputs the size of the response body in bytes
URL=$1; BODY_SIZE=$(curl -s -o /dev/null --write-out '%{size_download}' "$URL"); echo $BODY_SIZE
