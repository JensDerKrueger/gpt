def kaboom(i):
	print(i)
	if i < 3:
		kaboom(i+1)
	print(i)
	
kaboom(1)