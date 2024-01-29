#!/bin/bash
# This script sends a request to a specific URL and expects a certain response.
curl -sL -X PUT "0.0.0.0:5000/catch_me" -H "Origin: HolbertonSchool" -d "user_id=98"
