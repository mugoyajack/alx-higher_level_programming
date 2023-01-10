#!/usr/bin/python3
import sys
c = len(sys.argv) - 1
sum = 0
for i in range(c):
    sum = sum + int(sys.argv[1 + i])
print("{0}".format(sum))
