import sys

n = int(sys.argv[1])

i = 0
p = 1
while i <= n:
	print(i,p)
	i = i + 1
	p = p * 2
