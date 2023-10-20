# Assignment_On_Serverless_Architecture
Graded Assignment On Serverless Architecture
Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
Task: You're tasked to automate the stopping and starting of EC2 instances based on tags. Specifically:
1. Setup:
   - Create two EC2 instances.
   - Tag one of them as `Auto-Stop` and the other as `Auto-Start`.
2. Lambda Function Creation:
   - Set up an AWS Lambda function.
   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.
3. Coding:
   - Using Boto3 in the Lambda function:
     - Detect all EC2 instances with the `Auto-Stop` tag and stop them.
     - Detect all EC2 instances with the `Auto-Start` tag and start them.
4. Testing:
   - Manually invoke the Lambda function.
   - Confirm that the instance tagged `Auto-Stop` stops and the one tagged `Auto-Start` starts.
Instructions:
1. EC2 Setup:
   - Navigate to the EC2 dashboard and create two new t2.micro instances (or any other available free-tier type).
   - Tag the first instance with a key `Action` and value `Auto-Stop`.
   - Tag the second instance with a key `Action` and value `Auto-Start`.
2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonEC2FullAccess` policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Describe instances with `Auto-Stop` and `Auto-Start` tags.
     3. Stop the `Auto-Stop` instances and start the `Auto-Start` instances.
     4. Print instance IDs that were affected for logging purposes.
4. Manual Invocation:
   - After saving your function, manually trigger it.
   - Go to the EC2 dashboard and confirm that the instances' states have changed according to their tags.

Soln:-

IAM Role: israr_AmazonEC2FullAccess
Lambda Function: israr_ec2_start_stop
Instance ID
i-06fabeba5f7f137b3
i-03b5b77cd981d1e4e

EC2 Setup
1.	Navigate to the EC2 console: https://console.aws.amazon.com/ec2/v2/home.
2.	Click Launch Instance.
3.	Choose an Amazon Machine Image (AMI). I used the Ubuntu AMI.
4.	Choose an instance type. For example, I used the t2.micro instance type.
5.	Configure the instance details, such as the key pair and security group.
6.	Click Tag Instance.
7.	Add a tag with the key Action and value Auto-Stop.
8.	Click Launch Instance.
9.	Repeat steps 2-8 to create a second instance with the tag Action and value Auto-Start.
 

Lambda IAM Role
1.	Navigate to the IAM console: https://console.aws.amazon.com/iam/home.
2.	Click Roles.
3.	Click Create Role.
4.	Select AWS Lambda Basic Execution Role and click Next: Permissions.
5.	Select Add Permissions.
6.	Search for the AmazonEC2FullAccess managed policy and select it.
7.	Click Next: Review.
8.	Enter a name and description for the role I specified it as <israr_AmazonEC2FullAccess> and click Create Role.
 
 

Lambda Function
1.	Navigate to the Lambda console: https://console.aws.amazon.com/lambda/home.
2.	Click Create function.
3.	Select Author from scratch.
4.	Enter a name and description for the function.
5.	Select Python 3.8 as the runtime.
6.	Under Permissions, select Use an existing role and choose the IAM role you created in the previous step.
7.	Click Create function.
8.	In the code editor, paste the following Python script:

 
 

9.	Click Deploy.

Manual Invocation
1.	In the Lambda console, click the name of your function.
2.	Under Function overview, click Test.
3.	Click Invoke.
4.	Review the output in the Logs tab.
 
Confirmation
1.	Navigate to the EC2 console.
2.	Confirm that the instances' states have changed according to their tags.
 

################ End of the Task 1 ################

Assignment 17: Automated SNS Alerts for EC2 Disk Space Utilization
Objective: Set up a Lambda function that checks EC2 instances for disk space utilization, sending an SNS alert if utilization exceeds 85%.
Instructions:
1. Create a Lambda function.
2. Using Boto3, the function should:
   1. Connect to EC2 instances.
   2. Check disk space utilization.
   3. If disk space utilization exceeds 85%, publish a message to an SNS topic.
3. Set up a CloudWatch event to trigger this Lambda function daily.

Soln.:-

SNS: israr_DiskUtilization_SNS
IAM: israr_disk_utilization_check
Lambda: israr_disk_utilization_check
Cloudwatch Event Rules: israr_disk_utilization_check


To set up a Lambda function that checks EC2 instances for disk space utilization and sends an SNS alert if utilization exceeds 85%, follow these steps:

1. Create an SNS topic
1.	Navigate to the SNS console: https://console.aws.amazon.com/sns/v2/home.
2.	Click Create topic.
3.	Enter a name for the topic.
4.	Click Create topic.
 

2. Create an IAM role for the Lambda function
1.	Navigate to the IAM console: https://console.aws.amazon.com/iam/home.
2.	Click Roles.
3.	Click Create role.
4.	Select AWS Lambda Basic Execution Role and click Next: Permissions.
5.	Select Add Permissions.
6.	Search for the AmazonEC2FullAccess and AmazonSNSFullAccess managed policies and select them.
7.	Click Next: Review.
8.	Enter a name and description for the role and click Create Role.

 

3. Create the Lambda function
1.	Navigate to the Lambda console: https://console.aws.amazon.com/lambda/home.
2.	Click Create function.
3.	Select Author from scratch.
4.	Enter a name and description for the function.
5.	Select Python 3.8 as the runtime.
6.	Under Permissions, select Use an existing role and choose the IAM role you created in the previous step.
7.	Click Create function.
 

4. Write the Lambda function code
 

5. Deploy the Lambda function
Click the Deploy button to deploy the Lambda function.

6. To set up a CloudWatch event to trigger a Lambda function daily, you can follow these steps:
1.	Open the Functions page of the Lambda console.
2.	Choose the function that you want to trigger daily.
3.	Under Function overview, choose Add trigger.
4.	Set the trigger type to EventBridge (CloudWatch Events).
5.	For Rule, choose Create a new rule.
6.	Give the rule a name and a description.
7.	For Rule type, choose Schedule expression.
8.	Enter a cron expression that specifies the time and frequency of the trigger. For example, cron(0 12 * * ? *) will trigger the function every day at 12:00 UTC. You can use [this] tool to generate cron expressions easily.
9.	Choose Add.
 
 
7. Test the Lambda function
1.	In the Lambda console, click the name of your function.
2.	Under Function overview, click Test.
3.	Click Invoke.
4.	Review the output in the Logs tab.
8. Monitor SNS alerts
To monitor SNS alerts, you can subscribe to the SNS topic you created in step 1. You can receive alerts via email, SMS, or other notification channels.
Once you have completed these steps, your Lambda function will be triggered daily to check EC2 instances for disk space utilization and send an SNS alert if utilization exceeds 85%.

################ End of the Task 17 ################


Assignment 16: Implement a Log Cleaner for S3
Objective: Create a Lambda function that automatically deletes logs in a specified S3 bucket that are older than 90 days.
Instructions:
1. Create a new Lambda function.
2. Using Boto3, configure the function to:
   1. Access the specified S3 bucket.
   2. List all the log files.
   3. Check the age of each log.
   4. Delete logs older than 90 days.
3. Schedule this function to run weekly using AWS EventBridge.

Soln.:-

To create a Lambda function that automatically deletes logs in a specified S3 bucket that are older than 90 days, follow these steps:
1. Create a new Lambda function
1.	Navigate to the Lambda console: https://console.aws.amazon.com/lambda/home.
2.	Click Create function.
3.	Select Author from scratch.
4.	Enter a name and description for the function.
5.	Select Python 3.8 as the runtime.
6.	Under Permissions, select Use an existing role and choose an IAM role that has the necessary permissions to access the S3 bucket and delete objects.
7.	Click Create function.
2. Write the Lambda function code
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
  bucket_name = 'YOUR_S3_BUCKET_NAME'

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

3. Deploy the Lambda function
Click the Deploy button to deploy the Lambda function.
4. Schedule the Lambda function to run weekly using AWS EventBridge
1.	Navigate to the CloudWatch console: https://console.aws.amazon.com/cloudwatch/home.
2.	Click Events.
3.	Click Create rule.
4.	Enter a name and description for the rule.
5.	Under Event pattern, select Schedule.
6.	Enter a cron expression to trigger the Lambda function weekly. For example, the following cron expression will trigger the function at 12:00 AM every Sunday:
0 0 * * SUN
7.	Under Targets, click Add target.
8.	Select Lambda Function.
9.	Select the Lambda function you created in step 1.
10.	Click Add target.
11.	Click Create rule.
Once you have completed these steps, your Lambda function will be scheduled to run weekly and will automatically delete logs in the specified S3 bucket that are older than 90 days.

################ End of the Task 16 ################

Assignment 18: Restore EC2 Instance from Snapshot
Objective: Automate the process of creating a new EC2 instance from the latest snapshot using a Lambda function.
Instructions:
1. Create a Lambda function.
2. Using Boto3, the function should:
   1. Fetch the most recent snapshot of a given EC2 instance.
   2. Create a new EC2 instance using the fetched snapshot.
3. Trigger this Lambda function manually or on a schedule, depending on your recovery requirements.

Soln.:-

To automate the process of creating a new EC2 instance from the latest snapshot using a Lambda function, follow these steps:
1. Create a Lambda function
1.	Navigate to the Lambda console: https://console.aws.amazon.com/lambda/home.
2.	Click Create function.
3.	Select Author from scratch.
4.	Enter a name and description for the function.
5.	Select Python 3.8 as the runtime.
6.	Under Permissions, select Use an existing role and choose an IAM role that has the necessary permissions to access EC2 and Snapshots.
7.	Click Create function.
2. Write the Lambda function code
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
  snapshots = ec2.describe_snapshots(Filters=[{'Name': 'tag:Instance', 'Values': [instance_id]}]['Snapshots']
  latest_snapshot = sorted(snapshots, key=lambda snapshot: snapshot['StartTime'], reverse=True)[0]

  # Create a new EC2 instance using the fetched snapshot.
  new_instance = ec2.run_instances(ImageId=latest_snapshot['ImageId'], InstanceType='t2.micro')

  # Return the new instance ID.
  return new_instance['Instances'][0]['InstanceId']

3. Deploy the Lambda function
Click the Deploy button to deploy the Lambda function.
4. Trigger the Lambda function
You can trigger the Lambda function manually or on a schedule, depending on your recovery requirements.
To trigger the Lambda function manually:
1.	In the Lambda console, click the name of your function.
2.	Under Function overview, click Test.
3.	Under Event name, enter a name for the event.
4.	Under Payload, enter the following JSON:

{
  "instance_id": "YOUR_EC2_INSTANCE_ID"
}

5.	Click Invoke.
To trigger the Lambda function on a schedule:
1.	Navigate to the CloudWatch console: https://console.aws.amazon.com/cloudwatch/home.
2.	Click Events.
3.	Click Create rule.
4.	Enter a name and description for the rule.
5.	Under Event pattern, select Schedule.
6.	Enter a cron expression to trigger the Lambda function on a schedule. For example, the following cron expression will trigger the function at 12:00 AM every day:
              0 0 * * *
7.	Under Targets, click Add target.
8.	Select Lambda Function.
9.	Select the Lambda function you created in step 1.
10.	Click Add target.
11.	Click Create rule.
Once you have completed these steps, you will be able to automate the process of creating a new EC2 instance from the latest snapshot using a Lambda function.


################ End of the Task 18 ################

