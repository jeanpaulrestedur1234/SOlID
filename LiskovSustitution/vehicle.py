class Vehicle:
    def __init__(self, speed=0)-> None:
        
        self.speed = speed
    def acelerate(self, increment):
        self.speed += increment
        print(f"velocidad actual {self.speed}")
    
    def frenar(self, decrement):
        self.speed -= decrement
        if self.speed <=0:
            self.speed = 0
        print(f"velocidad actual {self.speed}")

class Car(Vehicle):
    def acelerate(self, increment):
         super().acelerate(increment)
    def frenar(self, decrement):
         super().frenar(decrement)
class Truck(Vehicle):
    def acelerate(self, increment):
         super().acelerate(increment)
    def frenar(self, decrement):
         super().frenar(decrement)
if __name__ == "__main__":
    car = Car()
    car.acelerate(1)
    car.frenar(1)