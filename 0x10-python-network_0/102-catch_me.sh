#!/bin/bash
# Send a POST request with specific data to trigger the expected response
curl -sLX PUT -d "user_id=98" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me
