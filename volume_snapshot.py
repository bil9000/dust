import boto3

#Describe your regions here
region_list = ['us-west-2']

#For creating snapshots


def create_snapshot(volume):
    Description='Created for volume '+volume
    client = boto3.client('ec2')
    response = client.create_snapshot(
        DryRun=False,
        VolumeId=volume,
        Description=Description
    )


def take_snapshots():
    client = boto3.client('ec2')
    #Iterate over regions listed
    for region in region_list:
        print("\n"+"#"*60+"  "+region+"  "+"#"*60+"\n")
        client = boto3.client('ec2', region_name=region)
        #Check for ElasticSearch Instances
        response = client.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['ElasticSearch']
                }
            ])
        #Iterate over instance(s)
        for r in response['Reservations']:
            for inst in r['Instances']:
                inst_id=inst['InstanceId']
                tags=inst['Tags']
                volumes=inst['BlockDeviceMappings']
                volume_name=[]
                #Iterate over instance's volume(s)
                for volume in volumes:
                    volume_name.append(volume)
                    print("Instance's volumes: ",volume_name)
                for volume in volumes:
                    volume=volume['Ebs']['VolumeId']
                    print("Creating snapshot for volume: ",volume)
                    t = create_snapshot(volume)


if __name__ == "__main__":
    try:
        take_snapshots()
    except Exception as err:
        print(err)