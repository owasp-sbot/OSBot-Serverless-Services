FROM python:3.12-bookworm

RUN pip install playwright
RUN playwright install --with-deps chromium

RUN pip install osbot-aws osbot-fast-api
RUN pip install requests mangum httpx
RUN pip install osbot-playwright

COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter

RUN python --version
ENV PORT=8080

WORKDIR /app
COPY ../../../osbot_serverless_flows /app/osbot_serverless_flows

ENV PYTHONPATH="/app"

COPY ./deploy/docker/osbot-serverless-flows__playwright/start.sh /app/start.sh

CMD ["./start.sh"]

