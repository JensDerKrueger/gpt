import sys

n = int(sys.argv[1])

for i in range(1, n+1):
	# i-te Zeile
	for j in range(1, n+1):
		# j-ter Eintrag in der i-ten Zeile
		if (i % j == 0) or (j % i == 0):
			print("* ",end="")
		else:
			print(". ",end="")
	print(i)