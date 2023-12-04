#!/bin/bash
# Send request using cURL and retrieve response body size in bytes
curl -s "$1" | wc -c
