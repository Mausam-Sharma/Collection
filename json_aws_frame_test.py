import json 

with open('test.json') as f:
    data = json.load(f)

length =len(data['Faces'])
for i in range(0,length):
  print(data['Faces'][i]['Face']['BoundingBox'])




