#!/bin/bash
URL=$1
BODY_SIZE=$(curl -s -o /dev/null --write-out '%{size_download}' "$URL")
echo $BODY_SIZE
