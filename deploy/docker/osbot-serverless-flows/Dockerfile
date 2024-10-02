FROM amazon/aws-lambda-python:3.12

ARG VERSION=${VERSION}

RUN echo "Installing version ${VERSION} of osbot_serverless_flows"

RUN pip install osbot_serverless_flows==${VERSION}
RUN pip install osbot-aws osbot-fast-api
RUN pip install requests mangum

CMD ["osbot_serverless_flows.lambdas.handler.run"]
