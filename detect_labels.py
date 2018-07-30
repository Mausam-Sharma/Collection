import boto3
from PIL import Image
import io
import os
import sys

client = boto3.client('rekognition')

# bucket = event['Records'][0]['s3']['bucket']['name']
# key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))

# fileName='Event/outfile.jpeg'
# bucket='mausamrest'
# bucket = event['Records'][0]['s3']['bucket']['name']
# fileName = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))

# response = rekognition.detect_labels(
# 	Image={"S3Object": {
#             "Bucket": "mausamrest",
#             "Name": "desk.jpg"
#         }},
# 	MinConfidence=95
# 	)

# leng=len(response)
# for x in range(0,leng):
# 	print(response['Labels'][x]['Name'])
local='images/desk.jpeg'
image = Image.open(local)
            
stream = io.BytesIO()
image.save(stream,format="JPEG")
image_binary = stream.getvalue()
        
response = client.detect_labels(
	Image={'Bytes':image_binary}
	)


print(response)