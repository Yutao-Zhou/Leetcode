from threading import Lock
class DiningPhilosophers:
    def __init__(self):
        self.forks = []
        for i in range(5):
            self.forks.append(Lock())
        

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5
        
        if philosopher % 2:
            self.forks[left_fork].acquire()
            self.forks[right_fork].acquire()
        else:
            self.forks[right_fork].acquire()
            self.forks[left_fork].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        if philosopher % 2:
            self.forks[left_fork].release()
            self.forks[right_fork].release()
        else:
            self.forks[right_fork].release()
            self.forks[left_fork].release()