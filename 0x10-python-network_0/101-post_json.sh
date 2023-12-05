#!/bin/bash
# sending JSON POST using curl from a file passed as args
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
