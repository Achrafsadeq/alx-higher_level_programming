#!/bin/bash
# Script that sends JSON POST request with contents of a file
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
