import json

import boto3

def lambda_handler(event, context):
  """Checks EC2 instances for disk space utilization and publishes an SNS alert if utilization exceeds 85%.
  Args:
    event: The Lambda event.
    context: The Lambda context.

  Returns:
    None.
  """
  # Initialize a boto3 EC2 client.
  ec2 = boto3.client('ec2')

  # Get a list of all EC2 instances.
  instances = ec2.describe_instances()['Reservations']

  # Iterate over all EC2 instances and check disk space utilization.
  for instance in instances:
    instance_id = instance['Instances'][0]['InstanceId']
    disk_space_utilization = ec2.describe_disks(InstanceIds=[instance_id])['Disks'][0]['UtilizationInPercent']

    # If disk space utilization exceeds 85%, publish an SNS alert.
    if disk_space_utilization > 85:
      sns = boto3.client('sns')
      sns.publish(TopicArn='YOUR_SNS_TOPIC_ARN', Message=f'Disk space utilization on EC2 instance {instance_id} exceeds 85%.')
