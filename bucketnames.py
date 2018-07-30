import boto3
from botocore.exceptions import ClientError

# bucket='mausamrest'
# key='data.txt'
s3 = boto3.client('s3')
s3_re = boto3.resource('s3')
for bucket in s3_re.buckets.all():
	s3_bucket = bucket
	s3_bucket_name = s3_bucket.name
	print(bucket)
	print(s3_bucket_name)
# s3 = boto3.client('s3')
# s3_re = boto3.resource('s3')
# bucket_tagging = s3_re.BucketTagging(bucket)
# try:
# 	response = s3.get_bucket_tagging(Bucket=bucket)
# except ClientError:
# 	print (bucket+ ",does not have tags, add tag")
# 	print("give key")
# 	inp_key = input()
# 	print("give value")
# 	inp_val = input()
# 	response = bucket_tagging.put(
#     	Tagging={
#         	'TagSet': [
#             	{
#                 	'Key': inp_key,
#                 	'Value': inp_val
#             	},
#         	]
#     	}
# 	)



