from collections import defaultdict

output = "Case #{}: {}".format

graph = defaultdict(list)

t = int(input())

for i in range(1, t+1):
	n = int(input())

	for _ in range(n):
		a, b = input().split()
		graph[[a, None]].append([b, None])
	
	print(graph)

