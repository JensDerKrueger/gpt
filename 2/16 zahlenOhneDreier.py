import sys

n = int(sys.argv[1])
for i in range(1, n+1):
	if i%3 != 0:
		print(i)
