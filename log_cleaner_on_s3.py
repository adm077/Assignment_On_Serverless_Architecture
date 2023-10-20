import boto3
def lambda_handler(event, context):
  """Automatically deletes logs in a specified S3 bucket that are older than 90 days.
  Args:
    event: The Lambda event.
    context: The Lambda context.
  Returns:
    None.
  """
  # Initialize a boto3 S3 client.
  s3 = boto3.client('s3')

  # Get the name of the S3 bucket.
  bucket_name = 'ISRAR_S3_BUCKET'

  # List all the objects in the S3 bucket.
  objects = s3.list_objects(Bucket=bucket_name)['Contents']

  # Iterate over all the objects and delete logs older than 90 days.
  for object in objects:
    object_key = object['Key']
    object_last_modified = object['LastModified']

    # Calculate the age of the object.
    object_age = (context.timestamp - object_last_modified.timestamp()) // 86400

    # Delete the object if it is older than 90 days.
    if object_age > 90:
      s3.delete_object(Bucket=bucket_name, Key=object_key)
