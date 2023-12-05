#!/bin/bash
# Send a POST request with specific data to trigger the expected response
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
