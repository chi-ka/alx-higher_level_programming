#!/bin/bash
# This script sends a POST request with specific data and displays the response
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
