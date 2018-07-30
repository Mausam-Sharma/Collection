import boto3
s3 = boto3.resource('s3')
bucket=s3.Bucket('mausamrest');
l=[]
print("enter list of keys: ")
a='y'
while(a=='y'):
	inp=input()
	l.append(inp)
	print('press y for more input')
	a=input()

length=len(l)
for obj in bucket.objects.all():
	for i in range[0,length]:
		if(obj.key==l[i]):
			print(obj)
	
