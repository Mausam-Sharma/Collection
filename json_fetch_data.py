import json 

with open('newtest.json') as f:
    data = json.load(f)

length =len(data['Persons'])


for i in range(0,length):
	try:
		print(data['Persons'][i]['FaceMatches'][0]['Similarity'])
		print(data['Persons'][i]['FaceMatches'][0]['Face']['FaceId'])
		print(data['Persons'][i]['Timestamp'])
	except:
		continue
