import sys
import math

p = float(sys.argv[1])
q = float(sys.argv[2])

d = p*p - 4.0*q
d = math.sqrt(d)

print((-p + d) / 2.0)
print((-p - d) / 2.0)
