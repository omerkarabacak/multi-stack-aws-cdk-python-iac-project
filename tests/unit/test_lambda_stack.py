import json
import pytest

from aws_cdk import core
from lambda_stack.lambda_stack import LambdaStack


def get_template():
    app = core.App()
    LambdaStack(app, "lambda-stack")
    return json.dumps(app.synth().get_stack("lambda-stack").template)


def test_s3_bucket_created():
    assert("AWS::S3::Bucket" in get_template())


def test_lambda_created():
    assert("AWS::Lambda::Function" in get_template())

def test_dynamodb_created():
    assert("AWS::DynamoDB::Table" in get_template())