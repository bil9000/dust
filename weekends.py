import boto3
import datetime
import schedule
import time


def job():
    client = boto3.client('ec2')
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
        Filters=[{
            'Name': 'tag:Weekends',
            'Values': [
                'Off'
            ]
        }])

    day0 = datetime.datetime.now()
    day1 = day0.isoweekday()

    if day1 == 6:
        for i in instances:
            print ("The time is now 7 pm on Friday.")
            print("It's Michelob time,we are shutting down ", i.id, i.instance_type)
            zulu = client.stop_instances(InstanceIds=[i.id])

    if day1 == 1:
        for i in instances:
            print("Happy monday we are starting the machines, grab some coffee", i.id, i.instance_type)
            berber = client.start_instances(InstanceIds=[i.id])


schedule.every().monday.at("07:00").do(job)
schedule.every().friday.at("19:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
