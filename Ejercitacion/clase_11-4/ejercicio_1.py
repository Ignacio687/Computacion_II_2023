#!/usr/bin/python3

'''Escribir un programa que realice la multiplicación de dos matrices de 2x2. 
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado 
en una fifo indicando el indice del elemento. El padre deberá leer en la fifo y mostrar el resultado final.'''

import os, time, sys, tempfile

class MultiProcessMatrixCalculator():
    def calculate(self, matrix1, matrix2):
        pidFather = os.getpid()
        pid = os.fork()
        child = 0
        for forkCount in range(1, 4):
            if pid != 0:
                pid = os.fork()
                child = forkCount
        if os.getpid() == pidFather:
            fd, tempfilename = tempfile.mkstemp()
            os.rename(tempfilename, 'fifo')
            #os.mkfifo('fifo')
            while True:
                time.sleep(1)
                with open('fifo', 'r') as fifo:
                    results = fifo.readlines()   
                if len(results) > 3:
                    sys.stdout.write(''.join(results))
                    os.remove('fifo')
                    break
        else:
            if child < 2:
                result = (matrix1[0][0]*matrix2[0][child])+(matrix1[0][1]*matrix2[1][child])
            else:
                result = (matrix1[1][0]*matrix2[0][child-2])+(matrix1[1][1]*matrix2[1][child-2])
            while True:
                if os.path.isfile('fifo'):
                    with open('fifo', 'a') as fifo:
                        if child < 2:
                            fifo.write(f'0{child}:{result}\n')
                        else:
                            fifo.write(f'1{child-2}:{result}\n')
                    break

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