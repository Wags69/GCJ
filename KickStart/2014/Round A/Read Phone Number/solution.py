from collections import OrderedDict

string = ''

def encoder(input_string):
	count = 1
	prev = ''
	lst = []
	for character in input_string:
		if character != prev:
			if prev:
				entry = (prev,count)
				lst.append(entry)
			count = 1
			prev = character
		else:
			count += 1
	else:
		try:
			entry = (character,count)
			lst.append(entry)
			return lst
		except Exception as e:
			print("Exception encountered {e}".format(e=e)) 
			return (e, 1)

numerals = { '0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five',
          '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine' }

names = { 2 : 'double', 3 : 'triple', 4 : 'quadruple', 5 : 'quintuple',
          6 : 'sextuple', 7 : 'septuple', 8 : 'octuple', 9 : 'nonuple', 10 : 'decuple' }

output = "Case #{}: {}".format

t = int(input())

for nim in range(1, t+1):
	p, cut = input().split()

	phone = list(p)
	frmt = list(map(int, cut.split('-')))

	lst = []

	for i in frmt:
		k = ''
		for _ in range(i):
			k += phone.pop(0)

		lst.append(k)

	arr = []

	for i in range(len(lst)):
		encoded = encoder(lst[i])
		for num, count in encoded:
			if count == 1:
				arr.append(numerals[num])
			elif count > 10:
				for i in range(count):
					arr.append(numerals[num])
			else:
				arr.append(names[count])
				arr.append(numerals[num])
				

	print(output(nim, ' '.join(arr)))
	phone = list(p)