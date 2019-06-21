output = "Case #{}: {}".format

#t = int(input())

#a = [int(input()) for _ in range(t)]

def switch(string):
	nstring = ""

	for i in string:
		if i == '1':
			nstring += '0'
		else:
			nstring += '1'

	return nstring

s = "0"

for _ in range(5):
	s = s + '0' + switch(s[::-1]) 
	print(s)

#for i, n in enumerate(a):