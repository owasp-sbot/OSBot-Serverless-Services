FROM python:3.12-slim

ARG VERSION=latest
#ARG DOCKER_FOLDER=./deploy/docker/osbot-serverless-flows

RUN echo "going to install version ${VERSION} of osbot-serverless-flows"
RUN pip install osbot_serverless_flows==${VERSION}

WORKDIR /app

#CMD ["python", "-m", "cbr_website_beta"]
CMD ["pip", "list"]
