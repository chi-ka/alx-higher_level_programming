#!/bin/bash

# Assign the first argument (URL) to a variable
URL=$1

# Use curl to get the body size and assign it to a variable
BODY_SIZE=$(curl -s -o /dev/null --write-out '%{size_download}' "$URL")

# Display the body size
echo $BODY_SIZE
