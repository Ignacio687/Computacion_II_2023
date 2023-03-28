#!/usr/bin/python3

import sys

def oddNumbersGenerator():
    try:
        n = int(sys.argv[2])
        strArg = sys.argv[1]
        sys.stdout.write(strArg*n)
    except:
        sys.stdout.write("This method requires two arguments, the first one can be any string and the second one an integer, which must be positive")

if __name__ == "__main__":
    oddNumbersGenerator()


#implementar libreria argparce y getopt