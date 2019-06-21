output = "Case #{}: {}".format

def is_sorted(a):
	for i in range(1, len(a)):
		if a[i] < a[i-1]:
			return False
	return True

t = int(input())
for l in range(t):
	n = int(input())
	a = [input() for _ in range(n)]

	m = 0 

	"""if l + 1 == 77:
					print(a)"""
  
	for i in range(1, len(a)):

		if is_sorted(a):
			break

		key = a[i]
		j = i - 1
		if key < a[j]:
			m += 1
		while j >= 0 and key < a[j] : 
			a[j+1] = a[j] 
			j -= 1
		a[j+1] = key 

	print(output(l+1, m))
	