#!/bin/bash

source .env

sed -E "s/AWS_ACCOUNT_ID/$AWS_ACCOUNT_ID/g" parameters.json > out/parameters.json

STACK_NAME=$(basename $(pwd))
STACK_NAME=$(echo $STACK_NAME | sed -E 's/_/-/g')

# cd parent_lambda/
# zip ../out/parent_function.zip -r .
# cd ..

cd child_lambda/
zip ../out/child_function.zip -r .
cd ..

# Upload the source code to an s3 bucket
aws cloudformation package \
    --template-file template.yml \
    --s3-bucket $S3_DEPLOY_BUCKET_NAME \
    --s3-prefix lambda-deploy-$STACK_NAME \
    --output-template-file out/template.yml

# Create a folder to output files, if any
aws s3api put-object \
    --bucket $S3_OUTPUT_BUCKET_NAME \
    --key lambda-deploy-$STACK_NAME-output/

# Deploy the stack
aws cloudformation deploy \
    --template-file out/template.yml \
    --stack-name $STACK_NAME \
    --parameter-overrides file://out/parameters.json
