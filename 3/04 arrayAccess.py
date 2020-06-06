# Deklaration
lottoZahlen = [2,18,4,19,5,47]

# komplette Ausgabe
print(lottoZahlen)

# direkt auf Elemente zugreifen
print(lottoZahlen[3])

# kann auch zum Schreiben genutzt werden
lottoZahlen[0] = 1
print(lottoZahlen)

# negative Indizes zählen von hinten (1-basiert)
lottoZahlen[-1] = 42
lottoZahlen[-2] = 3
print(lottoZahlen)

# Array Element für Element mittels Index ausgeben
for i in range(6):
	print(lottoZahlen[i])