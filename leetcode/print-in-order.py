from threading import Event

class Foo:
    def __init__(self):
        self.firstDone = Event()
        self.secondDone = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstDone.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.firstDone.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondDone.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.secondDone.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

from threading import Semaphore

class Foo:
    def __init__(self):
        self.gates = (Semaphore(False), Semaphore(False))


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.gates[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.gates[0]:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.gates[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.gates[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()

from threading import Lock

class Foo:
    def __init__(self):
        self.firstLock = Lock()
        self.secondLock = Lock()
        self.firstLock.acquire()
        self.secondLock.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstLock.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.firstLock:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.secondLock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.secondLock:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()