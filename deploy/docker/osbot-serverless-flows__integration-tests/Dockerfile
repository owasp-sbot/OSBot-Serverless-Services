FROM amazon/aws-lambda-python:3.12

RUN pip install osbot-aws requests

WORKDIR /app
COPY ../../../osbot_serverless_flows /app/osbot_serverless_flows

ENV PYTHONPATH="/app"



CMD ["osbot_serverless_flows.lambdas.handler.run"]
