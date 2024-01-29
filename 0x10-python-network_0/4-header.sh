#!/bin/bash
# This script sends a GET request to a given URL and displays the body of the response with a custom header
curl -s -H "X-School-User-Id: 98" "$1"
