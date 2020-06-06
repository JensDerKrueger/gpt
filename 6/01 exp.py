def exp(x,b):
    ergebnis = 1
    for i in range(x):
        ergebnis *= b
    return ergebnis

print(exp(0,2))
print(exp(1,2))
print(exp(2,2))

