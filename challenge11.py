# Crea una clase Punto2Dcon atributos x& y, y un método para imprimir sus coordenadas.



class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_coordenadas(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

# Ejemplo de uso
punto = Punto2D(3, 4)
punto.imprimir_coordenadas() 
