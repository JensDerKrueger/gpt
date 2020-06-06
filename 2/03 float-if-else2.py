import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

sum = a + b
print(a,"+",b,"=",sum)

diff = a - b
print(a,"-",b,"=",diff)

prod = a * b
print(a,"*",b,"=",prod)

if b != 0:
	quot   = a / b
	print(a,"/",b,"=",quot)
else:
	print(a,"/",b,"= nicht definiert") 

exp = a ** b
print(a,"**",b,"=",exp)