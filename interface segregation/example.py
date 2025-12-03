from abc import ABC, abstractmethod
## sin ISP


class WorkerInterface(ABC):
    @abstractmethod
    def work(self):
        print(" Worker is working")
        pass
    @abstractmethod
    def eat(self):
        print("Worker is eating")
        pass
    
    
class Human(WorkerInterface):
    def work(self):
        print("Human is working")
    
    def eat(self):
        print("Human is eating")

class Robot(WorkerInterface):
    def work(self):
        print("Robot is working")
    
    def eat(self):
        pass

##con Isp

class WorkerInterface(ABC):
    @abstractmethod
    def work(self):
        print(" working")

class EatInterface(ABC):
    @abstractmethod
    def eat(self):
        print(" eating")


class Human( WorkerInterface, EatInterface):
    
    def work(self):
        print("Human is working")
        super().work()
    def eat(self):
        print("Human is eating")
        super().eat()
    
class Robot(WorkerInterface):
    def work(self):
        print("Robot is working")
        
        super().work()
        

human= Human()
robot = Robot()
human.work()
human.eat()
robot.work()
try:
    robot.eat()
except:
    print("Robot does not have eat method")
    