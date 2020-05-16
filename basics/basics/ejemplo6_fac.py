# -*- coding: utf-8 -*-


def factorial(n):
    if(n > 0):
        return n*factorial(n-1)
    else:
        return 1


if __name__ == '__main__':
    number = int(raw_input('Ingresa un número: '))
    result = factorial(number)
    print(result)
