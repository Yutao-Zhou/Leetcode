from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.gates = [Lock(),Lock(),Lock()]
        self.gates[0].acquire()
        self.gates[1].acquire()
        self.terminate = False
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n * 2 + 1):
            self.gates[2].acquire()
            if i % 2 == 0 and (i // 2) % 2 == 1:
                self.gates[1].release()
            elif i % 2 == 0 and (i // 2) % 2 == 0:
                self.gates[0].release()
            else:
                printNumber(0)
                self.ct += 1
                self.gates[2].release()
        self.gates[2].acquire()
        self.terminate = True
        self.gates[0].release()
        self.gates[1].release()
        return

        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while 1:
            self.gates[0].acquire()
            if self.terminate:
                return
            printNumber(self.ct)
            self.gates[2].release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while 1:
            self.gates[1].acquire()
            if self.terminate:
                return
            printNumber(self.ct)
            self.gates[2].release()