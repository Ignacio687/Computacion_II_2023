import math, threading, queue

class TaylorCalculator():
    def __init__(self, terminos: int):
        self.terminos = terminos
        self.lifo = queue.Queue()
        self.barrier = threading.Barrier(self.terminos+1)
        self.lock = threading.Lock()

    def analyse(self, x, refValue):
        for thred in range(1, (self.terminos*2)+1, 2):
            th = threading.Thread(target=self.calculateTerm, args=(x, thred), daemon=True)
            th.start()
        th = threading.Thread(target=self.addTerms, args=(refValue,))
        th.start()
        th.join()
        print(f"El error es: {self.lifo.get()}")
        print(f"El resultado es: {self.lifo.get()}")

    def calculateTerm(self, x, thred):
        result = (1/math.factorial(thred))*(x**thred)
        with self.lock:
            self.lifo.put(result)
        self.barrier.wait()

    def addTerms(self, refValue):
        self.barrier.wait()
        result = 0
        for thred in range(0, (int(self.terminos/2))):
            result += self.lifo.get()
            result -= self.lifo.get()
        error = abs(result-refValue)
        self.lifo.put(error)
        self.lifo.put(result)

if __name__ == "__main__":
    app = TaylorCalculator(12)
    for x, error in [(0, 0.0), (0.7853981633974483, 0.7071067811865475), 
                     (1.5707963267948966, 1.0000000000000002), 
                     (3.141592653589793, -1.7028581387855716e-13)]:
        app.analyse(x, error)
        print("")
