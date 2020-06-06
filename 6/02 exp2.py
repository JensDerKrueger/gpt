def exp(x,b=2.718281828459045):
    ergebnis = 1
    for i in range(x):
        ergebnis *= b
    return ergebnis

print(exp(0,2))
print(exp(1,2))
print(exp(2,2))

print(exp(0))
print(exp(1))
print(exp(2))

print(exp(b=2, x=0))
print(exp(b=2, x=5))
print(exp(b=2, x=10))
