#!/bin/bash
# Script that sends request to URL and displays size of response body in bytes
curl -s "$1" | wc -c
