FROM amazon/aws-lambda-python:3.12

ARG VERSION=${VERSION}

RUN echo "Installing version ${VERSION} of osbot_serverless_flows"

RUN pip install osbot_serverless_flows==${VERSION} osbot-aws requests

CMD ["osbot_serverless_flows.lambdas.handler.run"]
