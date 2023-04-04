#!/usr/bin/python3

import os 
import sys
import math

class rootsCalculator:

    def __init__(self):
        self.Args = sys.argv
        if '-n' in  self.Args:
            self.number = int(self.Args[2])
        else:
            self.number = 0
        self.PPID = os.getpid()
        self.CPID = 0

    def calculate(self):
        if '-f' in self.Args:
            os.fork()
        if self.PPID == os.getpid():
            print(f'Parent PID: {self.PPID}')
            print(math.sqrt(self.number))
        else:
            self.CPID = os.getpid()
            print(f'Child PID: {self.CPID}')
            print(-math.sqrt(self.number))

if __name__ == '__main__':
    app = rootsCalculator()
    app.calculate()