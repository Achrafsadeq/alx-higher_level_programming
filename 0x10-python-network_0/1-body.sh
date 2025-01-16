#!/bin/bash
# Script that displays body of response only if status code is 200
curl -s -w "%{http_code}" "$1" -o /tmp/body.$$ 2>/dev/null | grep -q "200" && cat /tmp/body.$$ && rm -f /tmp/body.$$
