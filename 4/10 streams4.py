try:
	f = open("test.txt", "r")
	print(f.readlines())
	f.close()
except:
	print("Ich konnte die Datei test.txt nicht finden.")