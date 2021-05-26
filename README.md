# Multi-Stack AWS CDK Infrastructure as Code Project for Serverless and Container Projects
This project is an infrastructure as code (IaC) project for a serverless app and an ECS based container project

## Application Repositories

* serverless app: https://github.com/omerkarabacak/serverless-csv-to-dynamodb
* containerised app: https://github.com/omerkarabacak/containerised-python-flask-app

## How to run this AWS CDK Project

### Install CDK CLI tool

```
npm install -g aws-cdk
```

### How to create virtual environment for Python and install dependencies

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### How to run tests

```
pytest
```

### Show stacks

```
cdk ls
```

### How to deploy a selected stack

```
cdk deploy lambda-stack --profile <AWS_PROFILE_NAME>
```

### How to deploy all stacks

```
cdk deploy --all --profile <AWS_PROFILE_NAME>
```

### Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
