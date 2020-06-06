geheim = int(input("Gib eine geheime Zahl zwischen 1 und 100 ein: "))
print ("\n" * 100)
versuche = 1
geraten = int(input("Rate die geheime Zahl: "))

while geheim != geraten:
  if (geraten < geheim):
    print("zu klein")
  else:
    print("zu groß")
  geraten = int(input("Rate die geheime Zahl: "))
  versuche += 1

print("Super, Du hast sie nach " + str(versuche) + " Versuchen erraten!")

