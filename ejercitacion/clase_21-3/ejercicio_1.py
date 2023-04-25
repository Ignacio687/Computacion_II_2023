#!/usr/bin/python3

'''Escribir un programa en Python que acepte un número de argumento entero positivo n y genere una lista de 
los n primeros números impares. El programa debe imprimir la lista resultante en la salida estandar.'''

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