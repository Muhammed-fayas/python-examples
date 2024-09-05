#Project: Vehicle Management System

#Description: Create a program that manages different types of vehicles, including cars, trucks, and motorcycles.
#  Each vehicle should have attributes such as brand, model, year, and color. The program should also include methods to start the engine, accelerate, and brake.





class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand =brand
        self.model =model
        self.year =year
        self.color =color

    def start_engine(self):
        print("vroom")

    def accelerate(self):
        print("Accelerating...")

    def brake(self):
        print("braking...")


    #child classes:

    #car class:


class Car(Vehicle):
    def __init__(self, brand, model, year, color, num_doors):
        super().__init__(brand, model, year, color)
        self.num_doors=num_doors

    def open_trunk(self):
        print("trunk opened!")


    #Truck class:

class Truck(Vehicle):
    def __init__(self, brand, model, year, color, cargo_capacity):
        super().__init__(self, brand, model, year, color)
        self. cargo_capacity=cargo_capacity

    def load_cargo(self):
        print("loading cargo...")


    #motorcycle class


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, color, engine_size):
        super().__init__(brand, model, year, color)
        self.engine_size=engine_size
    
    def wheelie(self):
        print("Doing a wheelie")


    #main Program:


def main():
        car=Car("toyota" ,"corolla", 2015, "blue", 4)
        truck=Truck("Ford", "F-150", 2018 ,"Red", 1000)
        motorcycle=Motorcycle("Harley-Davidsom","Electra Glide", 2020, "Black",1200)
        
        car.start_engine()
        car.accelerate()
        car.brake()
        car.open_trunk()

        truck.start_engine()
        truck.accelerate()
        truck.brake()
        truck.load_cargo()

        motorcycle.start_engine()
        motorcycle.accelerate()
        motorcycle.brake()
        motorcycle.wheelie()

if __name__== "__main__": 
        main()