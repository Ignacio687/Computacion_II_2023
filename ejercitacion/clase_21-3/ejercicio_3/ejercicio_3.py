#!/usr/bin/python3

'''Escribir un programa en Python que acepte argumentos de línea de comando para leer un archivo de texto. 
El programa debe contar el número de palabras y líneas del archivo e imprimirlas en la salida estándar. 
Además el programa debe aceptar una opción para imprimir la longitud promedio de las palabras del archivo. 
Esta última opción no debe ser obligatoria. Si hubiese errores deben guardarse el un archivo cuyo nombre será 
"errors.log" usando la redirección de la salida de error.'''

import sys

def fileAnalyzer():
    sys.stderr = open('errorLog.txt', 'w')
    fileLines = sys.stdin.readlines()
    words = [0, 0, '']
    for line in fileLines:
        for letter in line:
            if letter != ' ':
                words[2] += letter
            elif words[2] != '':
                words[0] += 1
                words[1] += len(words[2])
                words[2] = ''
        if words[2] != '':
            words[0] += 1
            words[1] += len(words[2])
            words[2] = ''
    stdoutStr = f'Cantidad de lineas: {len(fileLines)}; cantidad de palabras: {words[0]}'
    if len(sys.argv) == 2:
        stdoutStr += f'; promedio de longitud de palabras: {words[1]//words[0]}' if sys.argv[1] == '-p' else ''
    sys.stdout.write(stdoutStr)


if __name__ == "__main__":
    fileAnalyzer()


#implementar libreria argparce y getopt