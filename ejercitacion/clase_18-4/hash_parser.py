'''Considerando el programa noblock.py, realizar un programa que lance dos procesos hijos que 
intenten encontrar el nonce para un No-Bloque con una dificultad dada. El hijo que lo encuentre 
primero debe comunicarse con el padre mediante una señal guardando el nonce en una fifo para que 
el padre pueda leerla. Hacer otra versión pero utilizando pipes.'''

import os, signal, psutil
from noblock import NoBlock



class HashParser():
    def __init__(self, fifoPath: str = "/", fifoName: str = "fifo",) -> None:
        self.fifopath = (fifoPath + fifoName)
        print(self.fifopath)
        os.mkfifo(self.fifopath)
        self.result = ''

    def run(self, seed: str, nonce: int = 0, difficulty: int = 1, childsAmount: int = 2):
        if self.mksubp(childsAmount):
            block = NoBlock(seed, nonce, difficulty)
            hash, nonce = block.proof_of_work()
            ppid = os.getppid()
            os.kill(ppid, 2)
            with open(self.fifopath, "a") as fifo:
                fifo.write(f'{nonce}\n{hash}')
        else:
            signal.signal(signal.SIGINT, self.readFifo)
            os.wait()
            return self.result

    def readFifo(self, uno, dos):
        with open(self.fifopath, "r") as fifo:
            result = fifo.readlines()
        os.unlink(self.fifopath)
        parent = psutil.Process(os.getpid())
        for child in parent.children(recursive=True):
            child.kill()
        self.result = f'nonce: {result[0]}\nhash: {result[1]}'

    def mksubp(self, childs):
        for child in range(0, childs):
            self.pid = os.fork()
            if self.pid == 0:
                return True
        return False
    
if __name__ == "__main__":
    app = HashParser(
        '/home/ignaciochaves/code/python/Computacion_II_2023/ejercitacion/clase_18-4/', 
        'fifo1')
    print(app.run(0, 5, 2))
