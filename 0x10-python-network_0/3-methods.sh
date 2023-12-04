#!/bin/bash
# retrieves all HTTP response methos allowed by the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
