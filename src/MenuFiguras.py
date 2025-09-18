from Figuras import Rectangulo, Cuadrado, Circulo, Triangulo #se importa de nuestro archivo las formulas de las figuras 
from blessed import Terminal # para ocupar los colores 

class MenuFiguras: # se empieza el codigo
    def __init__(self):
        self.term = Terminal()

    def validar_float(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor <= 0:
                    print(self.term.red("¡Error! El valor debe ser mayor que 0."))
                else:
                    return valor
            except ValueError:
                print(self.term.red("¡Error! Debes ingresar un número válido."))

    def mostrar_menu(self):
        print(self.term.bold_yellow("=== Menú de Figuras Geométricas ==="))
        print(self.term.green("1. Rectángulo"))
        print(self.term.blue("2. Cuadrado"))
        print(self.term.pink("3. Círculo"))
        print(self.term.orange("4. Triángulo"))
        print(self.term.red4("5. Salir"))
        
        opcion = input(self.term.bold_black("Elige una opción: "))
        return opcion

    def seleccionar_figura(self):
        while True:
            opcion = self.mostrar_menu()

            if opcion == "1":
                ancho = self.validar_float("Ingrese el ancho del rectángulo: ")
                alto = self.validar_float("Ingrese el alto del rectángulo: ")
                rectangulo = Rectangulo(ancho, alto)
                self.mostrar_resultados(rectangulo)
                
            elif opcion == "2":
                lado = self.validar_float("Ingrese el lado del cuadrado: ")
                cuadrado = Cuadrado(lado)
                self.mostrar_resultados(cuadrado)
                
            elif opcion == "3":
                radio = self.validar_float("Ingrese el radio del círculo: ")
                circulo = Circulo(radio)
                self.mostrar_resultados(circulo)
                
            elif opcion == "4":
                base = self.validar_float("Ingrese la base del triángulo: ")
                altura = self.validar_float("Ingrese la altura del triángulo: ")
                lado1 = self.validar_float("Ingrese el primer lado del triángulo: ")
                lado2 = self.validar_float("Ingrese el segundo lado del triángulo: ")
                triangulo = Triangulo(base, altura, lado1, lado2)
                self.mostrar_resultados(triangulo)

            elif opcion == "5":
                print(self.term.bold_blue2("¡Gracias por usar el programa!"))
                break

            else:
                print(self.term.red("Opción no válida. Inténtalo nuevamente."))

    def mostrar_resultados(self, figura):
        print(self.term.bold_cyan(f"\nResultados para {figura.__class__.__name__}:"))
        print(self.term.green3(f"Área: {figura.area():.2f}"))
        print(self.term.green3(f"Perímetro: {figura.perimetro():.2f}\n"))

if __name__ == "__main__":
    menu = MenuFiguras()
    menu.seleccionar_figura()
