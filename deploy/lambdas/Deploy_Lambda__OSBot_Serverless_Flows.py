from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Env import get_env, load_dotenv

from osbot_aws.AWS_Config import aws_config
from osbot_utils.base_classes.Type_Safe import Type_Safe

from osbot_aws.deploy.Deploy_Lambda import Deploy_Lambda
from osbot_serverless_flows.utils.Version import version__osbot_serverless_flows


class Deploy_Lambda__OSBot_Serverless_Flows(Type_Safe):
    lambda_name : str = 'osbot_serverless_flows'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_aws_credentials()
        self.deploy_lambda   = Deploy_Lambda(self.lambda_name)
        self.lambda_function = self.deploy_lambda.lambda_function()

    def lambda_deploy(self):
        self.lambda_setup()
        #self.deploy_lambda.deploy()
        self.lambda_setup_post_update()
        return self.lambda_invoke()

    def lambda_setup(self):
        self.deploy_lambda.set_container_image(self.ecr_image_uri())

    def lambda_setup_post_update(self):
        with self.lambda_function as _:
            if _.function_url_exists() is False:
                _.function_url_create_with_public_access()

    def lambda_invoke(self):
        with self.lambda_function as _:
            result = _.invoke()
            return result

    def ecr_image_uri(self):
        account_id  = aws_config.account_id()
        region_name = aws_config.region_name()
        image_name  = self.lambda_name
        image_tag   = version__osbot_serverless_flows
        return f'{account_id}.dkr.ecr.{region_name}.amazonaws.com/{image_name}:{image_tag}'

    def setup_aws_credentials(self):
        load_dotenv()
        aws_config.set_aws_session_account_id (get_env('AWS_ACCOUNT_ID__654654216424'       ))
        aws_config.set_region                 (get_env('AWS_DEFAULT_REGION__654654216424'   ))
        aws_config.set_aws_access_key_id      (get_env('AWS_ACCESS_KEY_ID__654654216424'    ))
        aws_config.set_aws_secret_access_key  (get_env('AWS_SECRET_ACCESS_KEY__654654216424'))
