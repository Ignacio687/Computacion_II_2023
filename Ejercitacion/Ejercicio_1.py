#! /usr/bin/python

import sys

def oddNumbersGenerator(n = sys.argv[1]):
    try:
        n = int(n)
        oddNumList = []
        while len(oddNumList) < n:
              oddNumList.append(len(oddNumList)+1)
        print(oddNumList)
        # sys.stdout.write(', '.join(oddNumList))
    except:
        sys.stdout.write("The argument must be a whole and positive integer")

if __name__ == "__main__":
    oddNumbersGenerator()