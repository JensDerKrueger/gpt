a = list(range(0,10))
print(a)

# ersetzt die ersten 3 Einträge
a[:3] = ["a", "b", "c"]
print(a)

# die Größen müssen nicht übereinstimmen
a[:3] = ["x"]
print(a)

# sie können auch größer sein
a[1:2] = ["x","y","z"]
print(a)

# oder sogar die leere Liste
a[4:] = []
print(a)

# natürlich auch auf beiden Seiten
a[1:2] = a[2:]
print(a)

# und auch von verschiedenen Arrays
b = [1.0,2.0,3.0,4.0]
print(b)
b[:3] = a[1:3]
print(b)