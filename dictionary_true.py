
data = dict()
def preprocess(s):
	for word in s.lower().split():
		data[word]='True'
	
    

s1 = 'This is a book'
text = preprocess(s1)
print (data)