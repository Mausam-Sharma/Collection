import boto3
s3Client = boto3.client('s3')
res=s3Client.generate_presigned_url('get_object', Params = {'Bucket': 'innovativevisioners', 'Key': 'desk.JPG'}, ExpiresIn = 100)
print(res)