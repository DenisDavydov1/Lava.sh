#!/bin/sh
location=$(curl -i -X "POST" -d '{"messages_to_send":[]}' -H "Content-Type: application/json" -H "Accept: application/json" https://jsonblob.com/api/jsonBlob | tr -d '\r' | sed -En 's/^location: (.*)/\1/p')
sed -i "s|location-here|${location}|" utils.py
