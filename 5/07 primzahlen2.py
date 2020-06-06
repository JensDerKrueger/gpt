def quadrat(n):
	return n*n

def istPrimzahl(n):
	if n < 2:
		return False
	i = 2
	while quadrat(i) <= n:
		if n % i == 0:
			return False
		i += 1
	return True
	
anzahl = 0
i = 2
while anzahl < 50:	
	if istPrimzahl(i):
		anzahl += 1
		print(anzahl,i)
	i += 1