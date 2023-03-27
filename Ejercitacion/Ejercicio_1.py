#!usr/bin/python3

import sys

def oddNumbersGenerator(n):
    try:
        oddNumList = [counter for counter in range(1, n+1, 2)]
        sys.stdout.write(oddNumList)
    except:
        sys.stdout.write("The argument must be a whole and positive integer")

if __name__ == "__main__":
    oddNumbersGenerator(sys.argv[1])