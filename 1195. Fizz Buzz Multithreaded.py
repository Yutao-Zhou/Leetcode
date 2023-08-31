import threading
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.mainLock = threading.Lock()
        self.fizzLock = threading.Lock()
        self.buzzLock = threading.Lock()
        self.fizzbuzzLock = threading.Lock()
        self.fizzLock.acquire()
        self.buzzLock.acquire()
        self.fizzbuzzLock.acquire()
        self.terminate = False

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	while 1:
            self.fizzLock.acquire()
            if self.terminate:
                return
            printFizz()
            self.mainLock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while 1:
            self.buzzLock.acquire()
            if self.terminate:
                return
            printBuzz()
            self.mainLock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while 1:
            self.fizzbuzzLock.acquire()
            if self.terminate:
                return
            printFizzBuzz()
            self.mainLock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.mainLock.acquire()
            if not i % 3 and i % 5:
                self.fizzLock.release()
            elif i % 3 and not i % 5:
                self.buzzLock.release()
            elif not i % 3 and not i % 5:
                self.fizzbuzzLock.release()
            else:
                printNumber(i)
                self.mainLock.release()
        self.mainLock.acquire()
        self.terminate = True
        self.fizzLock.release()
        self.buzzLock.release()
        self.fizzbuzzLock.release()
        return