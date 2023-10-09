# Lambda Function for Launching EC2 Instances and Scaling

This repository contains an AWS Lambda function written in Python that allows you to launch EC2 instances and scale them up using Auto Scaling. This Lambda function triggered by EventBridge (CloudWatch Events) to meet infrastructure scaling needs.

## Usage

### Environment Variables

The Lambda function relies on the following environment variables:

- `INSTANCE_TYPE`: The EC2 instance type you want to launch.
- `KEY_NAME`: The name of the EC2 key pair to associate with the instances.
- `AMI`: The ID of the Amazon Machine Image (AMI) you want to use for the instances.

#### EventBridge (CloudWatch Events)

This Lambda function is triggered by EventBridge (formerly known as CloudWatch Events). like this:

- Event bus: default
- Rule name: EC2testing
- Schedule expression: cron(0 10 * * ? *)  // triggers Everyday at 10:00am
- Service principal: events.amazonaws.com

### Scaling Up EC2 Instances

The Lambda function also includes code for scaling up EC2 instances using Auto Scaling. To use this feature:

1. Set the `auto_scaling_group_name` variable to the name of your Auto Scaling group.
2. Ensure that your Auto Scaling group is configured with appropriate scaling policies.
