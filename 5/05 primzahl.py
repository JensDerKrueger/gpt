import sys

def istPrimzahl(n):
	if n < 2: return False
	i = 2
	while i*i <= n:
		if n % i == 0: return False
		i += 1
	return True
	
zahl = int(sys.argv[1])
if istPrimzahl(zahl):
	print("Die Zahl",zahl,"ist eine Primzahl.")
else:
	print("Die Zahl",zahl,"ist keine Primzahl.")