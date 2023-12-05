#!/bin/bash
# send request passed as args
curl -s -o /dev/null -w "%{http_code}" "$1"
