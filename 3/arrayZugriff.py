# Array Element für Element ausgeben
for element in a:
	print(element)

# Länge des Arrays berechnen
länge = 0
for element in a:
	länge +=1
print(länge)

# ... oder mit eingebauter Funktion abfragen
print(len(a))

# Summe über die Elemente bestimmen
summe = 0
for element in a:
	summe += element
print(summe)

# ... oder mit eingebauter Funktion berechnen
print(sum(a))
