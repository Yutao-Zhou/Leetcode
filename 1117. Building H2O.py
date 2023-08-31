from threading import Lock
class H2O:
    #### Lock ####
    def __init__(self):
        self.h1 = Lock()
        self.h2 = Lock()
        self.o = Lock()
        self.h2.acquire()
        self.o.acquire()
        self.have_h = False


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        if self.have_h:
            self.h2.acquire()
        else:
            self.h1.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.have_h ^= True
        if not self.have_h:
            self.o.release()
        else:
            self.h2.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.h1.release()