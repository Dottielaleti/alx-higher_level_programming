#!/usr/bin/python3
for chr in range(97, 123):
    if chr != 'q' or chr != 'e':
         print("{:s}".format(chr(char + ord("a"))), end="")
