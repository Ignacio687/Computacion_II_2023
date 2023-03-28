#!/usr/bin/python3

import sys

def fileAnalyzer():
    sys.stderr = open('errorLog.txt', 'w')
    # with open(sys.stdin.readlines()) as f:
    #     fileLines = f.readlines()
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
    stdoutStr = f'Cantidad de lineas: {len(fileLines)}; cantidad de palabras: {len(words)}'
    if len(sys.argv) == 3:
        stdoutStr += f'; promedio de longitud de palabras: {words[1]/words[0]}' if sys.argv[2] == '-p' else ''
    sys.stdout.write(stdoutStr)


if __name__ == "__main__":
    fileAnalyzer()


#implementar libreria argparce y getopt