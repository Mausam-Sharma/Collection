from PIL import Image
import boto3

def lambda_handler(event, context):
	bucket = event['Records'][0]['s3']['bucket']['name']
	key = urllib.unquote_plus(
        	event['Records'][0]['s3']['object']['key'].encode('utf8'))

	s3 = boto3.client('s3')
	dynamodb = boto3.client('dynamodb')

	local = '/tmp/'+key
	s3.download_file(bucket,key, local)
	im = Image.open(local)

	width, height = im.size

	dynamodb.put_item(
    	TableName='dimension',
    	Item={
        	'keyname': {'S': key},
        	'height': {'N': height},
        	'width': {'N': width}
            })