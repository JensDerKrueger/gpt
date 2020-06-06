# ein Array definieren 
a = [1,2]

# komplett ausgeben
print(a)

# Elemente anhägen
a = a + [10]
print(a)

# ... in Kurzform
a += [7]
print(a)

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

# direkt auf Elemente zugreifen
print(a[3])
# kann auch zum Schreiben genutzte werden
a[2] = 42
print(a)

# Array Element für Element mittels Index ausgeben
for i in range(len(a)):
	print(a[i])

# letztes Element
print(a[-1])

# vorletztes Element (usw)
print(a[-2])

# Slicing "von":"bis"
print(a[1:2])

# Slicing "von" bis zum Ende
print(a[1:])

# kann auch zum Schreiben genutzte werden
a[0:2]=[100,200]
print(a)

# aus einer Range ein Array machen
b = list(range(10))
print(b)

# Arrays sind Referenzen
c = b
print(c)
c[0] = 100

print(c)
print(b)

# Deep Copy
d = c[:]
print(d)
d[0] = 500

print(d)
print(c)

