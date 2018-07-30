import boto3

client = boto3.client('s3')


response = client.get_object_acl(
    Bucket='mausamrest',
    Key='Capture.JPG'
    # VersionId='string',
    # RequestPayer='requester'
)
print(response['Grants'][0]['Permission'])