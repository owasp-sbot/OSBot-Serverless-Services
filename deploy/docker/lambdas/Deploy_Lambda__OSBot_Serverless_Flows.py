from osbot_aws.AWS_Config import aws_config
from osbot_utils.base_classes.Type_Safe import Type_Safe

from osbot_aws.deploy.Deploy_Lambda import Deploy_Lambda
from osbot_serverless_flows.utils.Version import version__osbot_serverless_flows


class Deploy_Lambda__OSBot_Serverless_Flows(Type_Safe):
    lambda_name : str = 'osbot_serverless_flows'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deploy_lambda = Deploy_Lambda(self.lambda_name)
        #self.lambda_       = self.deploy_lambda.lambda_function()

    def ecr_image_uri(self):
        account_id  = aws_config.account_id()
        region_name = aws_config.region_name()
        image_name  = self.lambda_name
        image_tag   = version__osbot_serverless_flows
        return f'{account_id}.dkr.ecr.{region_name}.amazonaws.com/{image_name}:{image_tag}'