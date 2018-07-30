import os
import boto3

s3 = boto3.resource('s3')

directory_in_str="E:\\streethack\\hold"

directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
    	
    	strg=directory_in_str+'\\'+filename
    	print(strg)
    	print("Enter name for your image : ")
    	inp_val = input()

    	strg2=inp_val+'.jpeg'
    	file = open(strg,'rb')
    	object = s3.Object('mausamrest','test/'+ strg2)
    	object.put(Body=file,ContentType='image/jpeg',ACL='public-read')
    	

        
    else:
        continue