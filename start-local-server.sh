#!/bin/bash

osbot_utils=${PWD}/modules/OSBot-Utils/

export PYTHONPATH=$osbot_utils:$PYTHONPATH

uvicorn osbot_serverless_flows.lambdas.handler:app --reload --host 0.0.0.0 --port 5005 \
                  --reload-dir $osbot_utils