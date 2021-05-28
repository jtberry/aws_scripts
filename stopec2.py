#!/usr/bin/python3

import boto3

def stop_all_ec2():

    # get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
                for region in ec2_client.describe_regions()['Regions']]
                
    # iterate over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        
        print("Region: {0}".format(region))
        
    # get only running instances
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name',
            'Values': ['running']}])
            
    for instance in instances:
        print("EC2 Instance: {0} is running in {1}".format(instance.id,region))
        
    # Stop ec2 instances
    for instance in instances:
        instance.stop()
        print("Stopping instance id: {0} in {1} region".format(instance.id, region))

if __name__ == "__main__":
    stop_all_ec2()