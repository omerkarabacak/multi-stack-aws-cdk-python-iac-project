#!/usr/bin/env python3

from aws_cdk import core

from lambda_stack.lambda_stack import LambdaStack
from container_stack.container_stack import ContainerStack

app = core.App()
LambdaStack(app, "lambda-stack")
ContainerStack(app, "container-stack")

app.synth()
