#!/usr/bin/python3

import sys

def oddNumbersGenerator():
    try:
        n = int(sys.stdin[1])
        oddNumList = [counter for counter in range(1, n*2, 2)]
        print(oddNumList)
        # sys.stdout.write(', '.join(oddNumList))
    except:
        sys.stdout.write("This method requires an argument, witch must be a whole and positive integer")

if __name__ == "__main__":
    oddNumbersGenerator()


#agregar libreria argparce y getopt