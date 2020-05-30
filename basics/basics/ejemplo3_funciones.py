# -*- coding:utf-8 -*-
from turtle import Turtle


def main():
    window = Turtle.Screen()
    leonardo = Turtle.turtle()

    make_square(leonardo)

    Turtle.mainloop()


def make_square(leonardo):
    length = int(input('Tamaño de cuadrado: '))
    for i in range(4):
        make_line_and_turn(leonardo, length)


def make_line_and_turn(leonardo, length):
    leonardo.forward(length)
    leonardo.left(90)


if __name__ == '__main__':
    main()
