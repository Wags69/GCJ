t = int(input())

for test_case in range(1, t+1):
	print('Case #{}:'.format(test_case), end=' ')

	trash = input()
	arr = [int(x) for x in input().split()]
	legend = []

	for i in arr:
		if i % 2 == 0:
			legend.append('e')
		else:
			legend.append('o')

	odd = [x for x in arr if x % 2 == 1]
	even = [x for x in arr if x %2 == 0]

	odd.sort()
	even.sort(reverse=True)

	arr2 = []

	for i in legend:
		if i == 'e':
			arr2.append(even.pop(0))
		else:
			arr2.append(odd.pop(0))

	print(' '.join(list(map(str, arr2))))
