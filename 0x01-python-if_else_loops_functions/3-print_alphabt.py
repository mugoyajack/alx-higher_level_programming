#!/usr/bin/python3
for a in range(97, 123):
    if chr(a) == 'q' or chr(a) == 'e':
        continue
    else:
        print("{0}".format(chr(a)), end="")
