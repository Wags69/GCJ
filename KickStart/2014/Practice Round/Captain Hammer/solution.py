import math

output = "Case #{}: {:.7f}".format

t = int(input())
a = [tuple(map(int, input().split())) for _ in range(t)]
g = 9.8

for i, pair in enumerate(a):
	v, d = pair
	boi = float('{:.15f}'.format((g * d)/(v**2)))
	theta = 0.5 * math.asin(boi)
	theta = theta * 180 / math.pi
	print(output(i+1, theta))
