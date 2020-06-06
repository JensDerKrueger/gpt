import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

sum    = a + b
diff   = a - b
prod   = a * b
if b != 0:
	quot   = a / b
exp    = a ** b

print(a,"+",b,"=",sum)
print(a,"-",b,"=",diff)
print(a,"*",b,"=",prod)
if b != 0:
	print(a,"/",b,"=",quot)
else:
	print(a,"/",b,"= nicht definiert") 
print(a,"**",b,"=",exp)