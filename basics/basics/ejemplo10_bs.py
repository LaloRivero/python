# -*- coding: utf-8 -*-
import random


def num_generator(n):
    i = 0
    arr = []
    while i < n:
        new_data = random.randint(0, 100000)
        try:
            arr.index(new_data)
        except ValueError:
            arr.append(new_data)
            i += 1

    arr.sort()
    print('')
    print('Puedes observar los datos para realizar las pruebas')
    print(arr)
    print('')
    return arr


def binary_search(data, search_num, low, high, cont):
    mid = (low+high)/2
    if data[mid] == search_num:
        print('Total de iteraciones {}'.format(cont))
        print('Correcto el número se encuentra en la lista')
    elif low > high:
        print('Total de iteraciones {}'.format(cont))
        print('Lo siento el número no fue encontrado')
    else:
        if search_num > data[mid]:
            cont += 1
            binary_search(data, search_num, mid+1, high, cont)
        else:
            cont += 1
            binary_search(data, search_num, low, mid-1, cont)


if __name__ == '__main__':
    n = int(raw_input("Ingresa cual sera la cantidad de datos: "))
    data = num_generator(n)
    search_num = int(raw_input('Ingresa el número que quieres buscar: '))
    binary_search(data, search_num, 0, len(data)-1, 0)
