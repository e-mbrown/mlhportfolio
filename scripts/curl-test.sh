#!/bin/sh

CONTENT='name=x&email=x&content=A Fresh test of curl script'
. ./.env

echo "Sending POST request to $URL/api/timeline_post"

POST= $(curl -s -X POST --max-time 1 "$URL/api/timeline_post" -d $CONTENT)

echo "Response: $POST"

echo "Sending GET request"

GET=$(curl "$URL/api/timeline_post") 

echo "Response: $GET"
# Compare post to get return error if not equal

echo "Sending DELETE request"

DELETE=$(curl -X DELETE "$URL/api/timeline_post/x")

echo "Result of DELETE request to $URL: $DELETE"

GET=$(curl "$URL/api/timeline_post") 

echo "Result of GET request to $URL: $GET"