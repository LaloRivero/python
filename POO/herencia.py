class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def print_type(self):
        print('La figura es un cuadrilatero')


class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)

    def print_cuadrado(self):
        print('Soy un cuadrado')


if __name__ == "__main__":
    rectangulo = Rectangulo(3, 4)
    print(rectangulo.area())

    cuadrado = Cuadrado(5)
    print(cuadrado.area())

    rectangulo.print_type()
    cuadrado.print_type()
    cuadrado.print_cuadrado()
