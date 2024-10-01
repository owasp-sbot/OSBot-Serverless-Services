FROM amazon/aws-lambda-python:3.12

ARG VERSION=${VERSION}

RUN echo "Installing version ${VERSION} of osbot_serverless_flows" \
    && pip install osbot_serverless_flows==${VERSION}

WORKDIR /app

COPY ./deploy/docker/osbot-serverless-flows/handler.py ${LAMBDA_TASK_ROOT}/


CMD ["handler.lambda_handler"]
