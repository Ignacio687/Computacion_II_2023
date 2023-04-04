#!/usr/bin/python3

import os 
import sys
import math

class rootsCalculator:

    def __init__(self):
        self.number = int(sys.argv[0])
        self.PPID = os.getpid()
        self.CPID = 0
        self.Args = sys.argv

    def calculate(self):
        if '-f' in self.Args:
            os.fork()
        if self.PPID == os.getpid():
            print('Parent PID: '+ self.PPID)
            print(math.sqrt(self.number))
        else:
            self.CPID = os.getpid()
            print('Child PID: '+ self.CPID)
            print(-math.sqrt(self.number))