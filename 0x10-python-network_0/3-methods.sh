#!/bin/bash
# This script displays all HTTP methods a server will accept for a given URL
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
