#Auto y Motor: Implementa una clase Auto que contenga 
# una instancia de una clase Motor con un método para describir el motor.
class Engine:
    def __init__(self, type, displacement):
        self.type = type
        self.displacement = displacement
        
    def describe_engine(self):
        return f"de tipo {self.type} y es de {self.displacement} cilindradas" 
    
class Car:
    def __init__(self, type, displacement):
        self.engine = Engine(type, displacement)
        
    def describe_car(self):
        return f"mi auto tiene un motor: {self.engine.describe_engine()}"
    
    
my_car = Car("Naftero", "1998")

print(my_car.describe_car())