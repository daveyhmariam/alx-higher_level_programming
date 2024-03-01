#!/bin/bash
#script that sends a JSON POST request to a URL passed as the first argument
curl -sH "content-type:application/json" -d "$(cat"$2")" "$1"
