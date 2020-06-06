import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

sum    = a + b
diff   = a - b
prod   = a * b
quot   = a // b
rest   = a % b
exp    = a ** b

print(a,"+",b,"=",sum)
print(a,"-",b,"=",diff)
print(a,"*",b,"=",prod)
print(a,"//",b,"=",quot)
print(a,"%",b,"=",rest)
print(a,"**",b,"=",exp)
