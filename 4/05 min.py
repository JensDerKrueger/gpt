import sys

n = int(sys.argv[1])
min = float(input())
for i in range(n-1):
    i = float(input())
    if i < max:
      min = i
print(min)
