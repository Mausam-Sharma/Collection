import boto3

s3 = boto3.resource('s3')
bucket=s3.Bucket('mausamrest')

for obj in bucket.objects.filter(Prefix='Event/'):
	print(obj.key)