t = int(input())

for case in range(1, t+1):
	print('Case #{}:'.format(case), end=' ')
	n = int(input())
	names = [input() for _ in range(n)]

	ndict = {}
	maximum = 0
	for name in names:
		s = set(name)
		s.discard(' ')

		ndict[name] = len(s)
		if len(s) > maximum:
			maximum = len(s)

	output = []

	for key, value in ndict.items():
		if value == maximum:
			output.append(key)

	output.sort()
	print(output[0])

