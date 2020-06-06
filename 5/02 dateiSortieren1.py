import sys

def speichern(ziel, namen):
	with open(ziel, "w") as zielDatei:
		zielDatei.writelines(namen)
	
quellenDateiname = sys.argv[1]
zielDateiname = sys.argv[2]

try:
	with open(quellenDateiname, "r") as quellDatei:
		namen = quellDatei.readlines()
	namen = sorted(namen)
	speichern(zielDateiname, namen)
except FileNotFoundError:
	print("Datei", quellenDateiname,
        "konnte nicht gefunden werden.")
except PermissionError:
	print("Es fehlen die notwendigen Rechte zum "
        "Lesen oder Schreiben.")