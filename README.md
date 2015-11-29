# dust

## the home of the random

## Weekends are back.

This is an automated script to turn non-essential servers on-and-off during your business hours.

[weekends.py] (Enjoy the weeekend.py) 

Hand crafted in boto3.



### de-splunk yerself

    hey hey hey.

I found a way to clean up your logs and store them in a few lines of code.

I guess I'll open source this.

First launch an ubuntu 14.04 box from AWS with roles that allow it to have Read Write Access to S3
'That is key.'

then create a bucket.

	aws s3 mb s3://somebucketname

	aws s3 sync /var/log/apache2/ s3://YOURBUCKETNAMEHERE

Ok, so that's all good, then we write a script to do the sync for the logs. (logUpload.sh)[logUpload.sh] The script is basically the following.

	#!/bin/bash
	aws s3 sync /var/log/apache2/ s3://YOURBUCKETNAMEHERE

Now you have to add the cron job to do this on a somewhat regular basis.

	crontab -e

In this file you need to put the times you want it to sync and n.b. you need to add the Path to your aws command line tools.

	PATH=/usr/local/bin/
	0 */3 * * * /home/ubuntu/logUpload.sh

That will sync the files every three hours to the bucket your made in the bucket s3://YOURBUCKETNAMEHERE

Now relax, knowing that your logs are shipped into s3 forever and ever amen.
	