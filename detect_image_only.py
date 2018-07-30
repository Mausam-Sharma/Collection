import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('mausamrest')

for o in bucket.objects.filter(Prefix='Event/test-event'):
	filename=o.key
	if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
		print(o.key)