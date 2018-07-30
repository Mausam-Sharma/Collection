import boto3
import random
s3 = boto3.client('s3')
source=boto3.resource('s3')

keys = []
resp = s3.list_objects_v2(Bucket='mausamrest')


for obj in resp['Contents']:
	keys.append(obj['Key'])

length = len(keys);
for x in range(0,length):
  #hello=random.randint(0,length)
  print (keys[x])
  #source.meta.client.download_file('mausamrest', keys[hello] , keys[hello])

