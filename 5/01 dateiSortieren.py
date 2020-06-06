import sys

quellenDateiname = sys.argv[1]
zielDateiname = sys.argv[2]
namen = []
try:
	# komplette Datei Einlesen
	with open(quellenDateiname, "r") as quellDatei:
		namen = quellDatei.readlines()
	
	# Sortieren
	namen = sorted(namen)
	
	# alles wieder Rausschreiben
	with open(zielDateiname, "w") as zielDatei:				
		zielDatei.writelines(namen)
		
except FileNotFoundError:
	print("Datei", quellenDateiname, "konnte nicht gefunden werden.")
except PermissionError:
	print("Es fehlen die notwendigen Rechte zum Lesen oder Schreiben.")
