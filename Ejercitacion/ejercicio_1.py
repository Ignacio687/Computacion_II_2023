#!/usr/bin/python3

import sys

def oddNumbersGenerator():
    try:
        n = int(sys.argv[1])
        oddNumList = [counter for counter in range(1, n*2, 2)]
        sys.stdout.write(str(oddNumList))
    except:
        sys.stdout.write("This method requires an argument, which must be a positive integer")


if __name__ == "__main__":
    oddNumbersGenerator()


#implementar libreria argparce y getopt