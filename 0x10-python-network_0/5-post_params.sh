#!/bin/bash
# Script that sends POST request with email and subject parameters
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
