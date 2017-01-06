#!/bin/bash

# Usage: slackpost <token> <channel> <message>

# Enter the name of your slack host here - the thing that appears in your URL:
# https://slackhost.slack.com/
slackhost="https://roystonfamily.slack.com"

token=

if [[ $token == "" ]]
then
        echo "No token specified"
        exit 1
fi

shift
channel="#traffic-bot-testing"
if [[ $channel == "" ]]
then
        echo "No channel specified"
        exit 1
fi

shift

text=$1

if [[ $text == "" ]]
then
        echo "No text specified"
        exit 1
fi

escapedText=$(echo $text | sed 's/"/\"/g' | sed "s/'/\'/g" )
json="{\"channel\": \"#$channel\", \"text\": \"$escapedText\"}"

curl -s -d "payload=$json" "https://$slackhost.slack.com/services/hooks/incoming-webhook?token=$token"
