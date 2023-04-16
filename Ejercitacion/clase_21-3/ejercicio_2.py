#!/usr/bin/python3

""" Escribir un programa en Python que acepte dos argumentos de línea de comando: una cadena de texto, un número 
entero. El programa debe imprimir una repetición de la cadena de texto tantas veces como el número entero. """

import sys

def inputMultiplier():
    try:
        n = int(sys.argv[2])
        strArg = sys.argv[1]
        sys.stdout.write(strArg*n)
    except:
        sys.stdout.write("This method requires two arguments, the first one can be any string and the second one an integer, which must be positive")

if __name__ == "__main__":
    inputMultiplier()


#implementar libreria argparce y getopt