#!/usr/bin/python3

import os 
import sys
import cmath
import argparse

class rootsCalculator:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog = 'rootsCalculator',
            description='calculate positive and negative roots of a number')
        self.parser.add_argument('n', type=int, help='the integer you want to know the square root of')
        self.parser.add_argument('-f', '--forkFlag', action='store_true', help='if you want the child process to calculate the negative square root')
        self.args = self.parser.parse_args()
        self.PPID = os.getpid()
        self.CPID = 0

    def calculate(self):
        if self.args.forkFlag:
            os.fork()
        if self.PPID == os.getpid():
            print(f'Parent PID: {self.PPID}')
            print(cmath.sqrt(self.args.n))
        else:
            self.CPID = os.getpid()
            print(f'Child PID: {self.CPID}')
            print(-cmath.sqrt(self.args.n))

if __name__ == '__main__':
    app = rootsCalculator()
    app.calculate()