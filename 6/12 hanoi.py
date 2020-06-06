def hanoi(quelle, zwischenlager, ziel, scheibe):
	if scheibe > 0:
		hanoi(quelle, ziel, zwischenlager, scheibe-1)
		print("Lege Scheibe",scheibe,"von",quelle,"nach",ziel)
		hanoi(zwischenlager, quelle, ziel, scheibe-1)
	
hanoi(1,2,3,4)
