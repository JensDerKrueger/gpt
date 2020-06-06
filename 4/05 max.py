import sys

n = int(sys.argv[1])
max = float(input())
for i in range(n-1):
    i = float(input())
    if i > max:
      max = i
print(max)
