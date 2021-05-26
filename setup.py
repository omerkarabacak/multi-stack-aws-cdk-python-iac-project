import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="multi_stack",
    version="0.0.1",

    description="A CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "lambda_stack","":"container_stack"},
    packages=setuptools.find_packages(where="lambda_stack,container_stack"),

    install_requires=[
        "aws-cdk.core==1.106.0",
        "aws-cdk.aws_s3==1.106.0",
        "aws-cdk.aws_lambda==1.106.0",
        "aws-cdk.aws_dynamodb==1.106.0",
        "aws-cdk.aws_iam==1.106.0",
        "aws_cdk.aws_lambda_event_sources==1.106.0",
        "aws_cdk.aws_ecr==1.106.0",
        "aws_cdk.aws_ecs==1.106.0",
        "aws_cdk.aws_ecs_patterns==1.106.0",
        "aws_cdk.aws_ec2==1.106.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
