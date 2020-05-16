# -*- coding:utf-8 -*-
import turtle


def main():
    window = turtle.Screen()
    leonardo = turtle.Turtle()

    make_square(leonardo)

    turtle.mainloop()


def make_square(leonardo):
    length = int(raw_input('Tamaño de cuadrado: '))
    for i in range(4):
        make_line_and_turn(leonardo, length)


def make_line_and_turn(leonardo, length):
    leonardo.forward(length)
    leonardo.left(90)


if __name__ == '__main__':
    main()
