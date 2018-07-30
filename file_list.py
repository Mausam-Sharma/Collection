import boto3
s3 = boto3.resource('s3')
bucket=s3.Bucket('mausamrest');
obj = s3.Object('mausamrest','do-not-delete-folder/delete-this-folder/')
counter=-1


for obj in bucket.objects.filter(Prefix='do-not-delete-folder/delete-this-folder/'):
	print(obj.key)
	try:
		obj.delete()
		counter=counter+1
	except:
		print("error occurred while deleting")

if(counter==-1):
	print("subfolder doesn't exists")
if(counter!=-1):
	print("1 subfolder and "+str(counter)+" items in it deleted")
# except:
# 	print("subfolder doesn't exists")



# if(counter!=0):
# 	obj.delete()
# print(counter)