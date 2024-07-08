# Polimorfismo: Crea una clase base Animalcon un método
# hacerSonidoy una clase derivada Perroque sobrescriba este método.


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"Hola, mi nombre es {self.name} y hago {self.sound} ")
        


class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        
animal1 = Dog("perro", "guau guau")
animal1.make_sound()