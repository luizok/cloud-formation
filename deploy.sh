#!/bin/bash

source .env

sed -E "s/AWS_ACCOUNT_ID/$AWS_ACCOUNT_ID/g" parameters_template.json > parameters.json

STACK_NAME=$(basename $(pwd))
STACK_NAME=$(echo $STACK_NAME | sed -E 's/_/-/g')

# echo $STACK_NAME
# read ans

aws cloudformation deploy \
    --template-file template.yml \
    --stack-name $STACK_NAME \
    --parameter-overrides file://parameters.json
