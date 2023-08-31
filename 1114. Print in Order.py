import threading
class Foo:
    def __init__(self):
        self.firstFinished = threading.Lock()
        self.secondFinished = threading.Lock()
        self.firstFinished.acquire()
        self.secondFinished.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstFinished.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.firstFinished.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondFinished.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.secondFinished.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()