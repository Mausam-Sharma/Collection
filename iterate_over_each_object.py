from __future__ import print_function

import boto3
import io
import uuid
import urllib
from PIL import Image
import datetime
from pprint import pprint


def lambda_handler(event, context):
	rekognition = boto3.client('rekognition')
	dynamodb = boto3.client('dynamodb')
	s3 = boto3.resource('s3')
	s3client=boto3.client('s3')

	Bucket=s3.Bucket('ais-django')
	obj = s3.Object('ais-django','Event/')

	i = datetime.datetime.now()
	ptr= i.strftime("%d-%m-%y     %H:%M:%S (UTC)")

	for obj in Bucket.objects.filter(Prefix='Event/'):
		filename=obj.key
		if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
			key=str(filename)
			bucket='ais-django'
			print(key)

			local = '/tmp/'+ptr+'.jpeg'
			
			s3client.download_file(bucket,key, local)

			image = Image.open(local)
			stream = io.BytesIO()
			image.save(stream,format="JPEG")

			image_binary = stream.getvalue()
			response = rekognition.detect_faces(
				Image={'Bytes':image_binary}
				)


			all_faces=response['FaceDetails']

			boxes = []
			image_width = image.size[0]
			image_height = image.size[1]

			for face in all_faces:
				box=face['BoundingBox']
				x1 = int(box['Left'] * image_width) * 0.9
				y1 = int(box['Top'] * image_height) * 0.9
				x2 = int(box['Left'] * image_width + box['Width'] * image_width) * 1.10
				y2 = int(box['Top'] * image_height + box['Height']  * image_height) * 1.10
				image_crop = image.crop((x1,y1,x2,y2))

				stream = io.BytesIO()
				image_crop.save(stream,format="JPEG")
				image_crop_binary = stream.getvalue()

				response = rekognition.search_faces_by_image(
					CollectionId='family_collection',
					Image={'Bytes':image_crop_binary}
					)

				if len(response['FaceMatches']) > 0:

					for match in response['FaceMatches']:
						face = dynamodb.get_item(
							TableName='family_collection',
							Key={'RekognitionId': {'S': match['Face']['FaceId']}}
							)
						if 'Item' in face:
							person = face['Item']['FullName']['S']
							print(person);
							ktr='results/'+person+'.jpg'
							s3client.upload_file(local, 'ais-django', ktr,ExtraArgs={'ContentType': 'image/jpeg','ACL': 'public-read'})
							dynamodb.put_item(
                    			TableName='results',
                    			Item={
                         			'image': {'S': key},
                         			'FullName': {'S': person},
                         			'date': {'S': ptr}
                    			}
                			)								
				else:
					print('null')

            
            
            	
            		
            		
            		
            	
            		
            		
