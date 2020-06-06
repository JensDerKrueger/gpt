import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

sum    = a + b
diff   = a - b
prod   = a * b
quot   = a / b
exp    = a ** b

print(a,"+",b,"=",sum)
print(a,"-",b,"=",diff)
print(a,"*",b,"=",prod)
print(a,"/",b,"=",quot)
print(a,"**",b,"=",exp)
