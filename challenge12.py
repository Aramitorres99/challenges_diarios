# Crea una clase base Figuracon un método imprimiry una clase derivada Círculo
# que extiende Figura y sobreescribe el método imprimir.


class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    def imprimir_figura(self):
        print(f'Hola soy un {self.nombre}')
        
class Circulo(Figura):
    
    def imprimir_figura(self):
        return super().imprimir_figura()
    

figura1 = Figura('circulo')

figura2 = Circulo('cuadrado')

figura2.imprimir_figura()
