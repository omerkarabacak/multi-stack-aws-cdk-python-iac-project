from aws_cdk import (
    aws_dynamodb as _dynamodb,
    aws_s3 as _s3,
    aws_lambda as _lambda,
    aws_iam as _iam,
    core
)

from aws_cdk.aws_lambda_event_sources import S3EventSource


class LambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        serverless_db = _dynamodb.Table(self, id='dynamoTable', table_name='csv-table',
                                        partition_key=_dynamodb.Attribute(name='name', type=_dynamodb.AttributeType.STRING))

        serverless_bucket = _s3.Bucket(
            self, id='s3bucket', bucket_name='csv-bucket-2021')

        serverless_lambda = _lambda.Function(self,
                                             id='csv_to_dynamodb',
                                             runtime=_lambda.Runtime.PYTHON_3_8,
                                             handler='app.lambda_handler',
                                             code=_lambda.Code.from_inline(
                                                 ' '),
                                             role=_iam.Role.from_role_arn(
                                                 self, id='lambda_role', role_arn='arn:aws:iam::906440755908:role/service-role/csv_to_dynamodb-role-jkk1lpey')
                                             )
        serverless_lambda.add_event_source(S3EventSource(serverless_bucket,
                                                         events=[
                                                             _s3.EventType.OBJECT_CREATED]
                                                         ))
