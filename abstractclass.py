from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(computer):
    def process(self):
        print("its running")
        

class whiteboard:
    def write(self):
        print("its wriring")

class programmer:
    def work(self):
        print("solving bugs")
        com1.process()

com1=Laptop()
com1.process()
prog1=programmer()
prog1.work()
