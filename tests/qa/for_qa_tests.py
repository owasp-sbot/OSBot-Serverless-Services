from osbot_utils.utils.Env import get_env

ENV_VAR_NAME__QA_LAMBDA        = 'ENDPOINT_URL__QA_LAMBDA'
ENDPOINT_URL__QA_LAMBDA        = 'https://serverless-flows.dev.aws.cyber-boardroom.com'
ENDPOINT_URL__USE_DEV_SERVER   = False


if ENDPOINT_URL__USE_DEV_SERVER:                                        # todo: add check (when this is set) that the local server is online
    qa__endpoint_url = get_env(ENV_VAR_NAME__QA_LAMBDA, ENDPOINT_URL__QA_LAMBDA)
else:
    qa__endpoint_url = ENDPOINT_URL__QA_LAMBDA