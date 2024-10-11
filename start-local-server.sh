#!/bin/bash

uvicorn osbot_serverless_flows.lambdas.handler:app --reload --host 0.0.0.0 --port 5005