from threading import Barrier, Semaphore

class H2O:
    def __init__(self):
        self.barrier = Barrier(3)
        self.h_sem = Semaphore(2)
        self.o_sem = Semaphore(1) # could also be lock?

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h_sem.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o_sem.release()

from threading import Barrier, Semaphore

class H2O:
    def __init__(self):
        self.barrier = Barrier(3)
        self.h_sem = Semaphore(2)
        self.o_sem = Semaphore(1) # could also be lock?

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.h_sem:
            self.barrier.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.o_sem:
            self.barrier.wait()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()

from threading import Barrier, Semaphore, Lock

class H2O:
    def __init__(self):
        self.barrier = Barrier(3)
        self.h_sem = Semaphore(2)
        self.o_lock = Lock()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.h_sem:
            self.barrier.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.o_lock:
            self.barrier.wait()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()

from threading import Barrier, Semaphore, Lock

class H2O:
    def __init__(self):
        self.barrier = Barrier(3)
        self.h_sem = Semaphore(2)
        self.o_lock = Lock()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h_sem.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_lock.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o_lock.release()