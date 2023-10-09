#lambda to luanch EC2

import boto3
import os
ec2 = boto3.resource('ec2')
autoscaling = boto3.client('autoscaling')

INSTANCE_TYPE = os.environ['INSTANCE_TYPE']  #These will be environment variables that we must specify in lambda
KEY_NAME = os.environ['KEY_NAME']
AMI=os.environ['AMI']


def lambda_handler(event, context):   #Start of our function
    instance = ec2.create_instances(
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        ImageId=AMI,
        MaxCount=1,
        MinCount=1,
        TagSpecifications=[{    #This creates a tag for our resource
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name','Value': 'test'}]
        }]   
    )
    
def lambda_handler(event, context):
    auto_scaling_group_name = 'EC2Lambdatesting'
    response = autoscaling.set_desired_capacity(
        AutoScalingGroupName = auto_scaling_group_name,
        DesiredCapacity = 2
        )
    return{
        'statusCode' : 200,
        'body' : 'Scaling up EC2 instances'
    }
    
    print("New instance created:", instance[0].id)
