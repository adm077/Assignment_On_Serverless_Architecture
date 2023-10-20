import boto3
def lambda_handler(event, context):
  """Creates a new EC2 instance from the latest snapshot of a given EC2 instance.
  Args:
    event: The Lambda event.
    context: The Lambda context.
  Returns:
    None.
  """

  # Initialize a boto3 EC2 client.
  ec2 = boto3.client('ec2')

  # Get the instance ID from the event.
  instance_id = event['instance_id']

  # Fetch the most recent snapshot of the instance.
  snapshots = ec2.describe_snapshots(Filters=[{'Name': 'tag:Instance', 'Values': [instance_id]}]['Snapshots'])
  latest_snapshot = sorted(snapshots, key=lambda snapshot: snapshot['StartTime'], reverse=True)[0]

  # Create a new EC2 instance using the fetched snapshot.
  new_instance = ec2.run_instances(ImageId=latest_snapshot['ImageId'], InstanceType='t2.micro')

  # Return the new instance ID.
  return new_instance['Instances'][0]['InstanceId']
