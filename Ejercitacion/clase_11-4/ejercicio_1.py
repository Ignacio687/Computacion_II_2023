#!/usr/bin/python3

'''Escribir un programa que realice la multiplicación de dos matrices de 2x2. 
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado 
en una fifo indicando el indice del elemento. El padre deberá leer en la fifo y mostrar el resultado final.'''

import os, time, sys

class MultiProcessMatrixCalculator():
    def calculate(self, matrix1, matrix2):
        os.mkfifo('fifo')
        pidFather = os.getpid()
        pid = os.fork()
        child = 0
        for forkCount in range(1, 4):
            if pid != 0:
                pid = os.fork()
                child = forkCount
        if os.getpid() == pidFather:
            while True:
                time.sleep(0.2)
                with open('fifo', 'r') as fifo:
                    results = fifo.readlines()
                if len(results) > 3:
                    sys.stdout.write(''.join(results))
                    os.remove('fifo')
                    break
        else:
            row = 0 if child < 2 else 1
            col = 0 if child == 0 or child == 2 else 1
            result = 0
            for rowAndColCount in range (0, len(matrix1[0])):
                result += (matrix1[row][rowAndColCount] * matrix2[rowAndColCount][col])
            with open('fifo', 'a') as fifo:
                fifo.write(f'{row}{col}:{result}\n')


if __name__=='__main__':
    matrixList = [
        [
        [5, 2],
        [8, 7]
        ],[
        [2, 3],
        [6, 4]
        ]
    ]
    calculator = MultiProcessMatrixCalculator()
    calculator.calculate(matrixList[0], matrixList[1])