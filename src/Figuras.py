class Rectangulo:
    def __init__(self, ancho: float, alto: float): 
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    
class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

    def perimetro(self):
        return 2 * 3.1416 * self.radio

class Triangulo:
    def __init__(self, base: float, altura: float, lado1: float, lado2: float):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado1 + self.lado2
