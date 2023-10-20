import boto3

import json

def lambda_handler(event, context):
    """Detects and starts/stops EC2 instances with the Auto-Stop and Auto-Start tags."""

    # Create a Boto3 EC2 client.
    ec2 = boto3.client('ec2')

    # Get all EC2 instances with the Auto-Stop tag.
    auto_stop_instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Auto-Stop',
                'Values': ['Yes']
            }
        ]
    )['Reservations']

    # Stop all EC2 instances with the Auto-Stop tag.
    for instance in auto_stop_instances:
        instance_id = instance['Instances'][0]['InstanceId']
        ec2.stop_instances(InstanceIds=[instance_id])

    # Get all EC2 instances with the Auto-Start tag.
    auto_start_instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Auto-Start',
                'Values': ['Yes']
            }
        ]
    )['Reservations']

    # Start all EC2 instances with the Auto-Start tag.
    for instance in auto_start_instances:
        instance_id = instance['Instances'][0]['InstanceId']
        ec2.start_instances(InstanceIds=[instance_id])

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully started/stopped EC2 instances.')
    }