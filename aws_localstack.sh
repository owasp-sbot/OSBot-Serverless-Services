#!/bin/bash

# Define the LocalStack endpoint and dummy AWS credentials
LOCALSTACK_URL="http://localhost:4566"
AWS_ACCESS_KEY_ID="dummy"
AWS_SECRET_ACCESS_KEY="dummy"
AWS_DEFAULT_REGION="us-east-1"

# Export the credentials and region environment variables for AWS CLI
export AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY
export AWS_DEFAULT_REGION

# Check if the service needs an endpoint URL (can be expanded for more services)
case "$1" in
  s3|lambda|dynamodb|sns|sqs|sts|cloudformation|logs)
    # Add the --endpoint-url option for the supported services
    aws --endpoint-url="$LOCALSTACK_URL" "$@"
    ;;
  *)
    # For other commands, just pass them through to aws as-is
    aws "$@"
    ;;
esac
