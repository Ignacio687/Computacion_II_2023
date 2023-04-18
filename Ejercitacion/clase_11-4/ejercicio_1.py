#!/usr/bin/python3

'''Escribir un programa que realice la multiplicación de dos matrices de 2x2. 
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado 
en una fifo indicando el indice del elemento. El padre deberá leer en la fifo y mostrar el resultado final.'''

import os, time, sys

class MultiProcessMatrixCalculator():
    def run(self, matrix1, matrix2):
        os.mkfifo('fifo')
        pid = 1
        for forkCount in range(0, 5):
            #Child Process calculations and fifo write
            if pid == 0:
                row = 0 if child < 2 else 1
                col = 0 if child % 2 == 0 else 1
                result = 0
                for rowAndColCount in range (0, 2):
                    result += (matrix1[row][rowAndColCount] * matrix2[rowAndColCount][col])
                with open('fifo', 'a') as fifo:
                    fifo.write(f'{row}{col}:{result}\n')
                os._exit(0)
            #Parent Process fifo read
            elif forkCount == 4:
                while True:
                    time.sleep(0.2)
                    with open('fifo', 'r') as fifo:
                        results = fifo.readlines()
                    if len(results) > 3:
                        sys.stdout.write(''.join(results))
                        os.unlink('fifo')
                        break
            #Parent Process child generation
            else:
                pid = os.fork()
                child = forkCount



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
    app = MultiProcessMatrixCalculator()
    stringTest = app.run(matrixList[0], matrixList[1])