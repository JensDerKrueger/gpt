import sys

n = int(sys.argv[1])
p = 1

# bei nur einem Parameter startet range bei 0
for i in range(n+1):
	print(i,p)
	p = p * 2

