from aws_cdk import (
    aws_ecr as _ecr,
    aws_ecs as _ecs,
    aws_ec2 as _ec2,
    aws_ecs_patterns as _ecs_patterns,
    core
)


class ContainerStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        containerised_app_repository = _ecr.Repository(self, "Containerised-App-Repository")

        # default is all AZs in region
        containerised_app_vpc = _ec2.Vpc(self, "Containerised-App-VPC", max_azs=2)

        containerised_app_cluster = _ecs.Cluster(self, "Containerised-App-ECS-Cluster", vpc=containerised_app_vpc)

        containerised_app_ecs_application = _ecs_patterns.ApplicationLoadBalancedFargateService(self, "Containerised-App-Fargate-Service",
                                                           cluster=containerised_app_cluster,
                                                           cpu=256,
                                                           desired_count=2,
                                                           task_image_options=_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                               image=_ecs.ContainerImage.from_registry('amazon/amazon-ecs-sample')),
                                                           memory_limit_mib=512,
                                                           public_load_balancer=True)
        containerised_app_repository.grant_pull(containerised_app_ecs_application.task_definition.obtain_execution_role())
