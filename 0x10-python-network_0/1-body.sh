#!/bin/bash
# Script that displays body of response only if status code is 200
curl -s "$1" -I | grep -q "200 OK" && curl -s "$1"
