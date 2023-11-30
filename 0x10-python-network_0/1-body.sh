#!/bin/bash
# Displays the size of the body of the response
curl -sI "$1" | grep "200" | cut -d' ' -f3
