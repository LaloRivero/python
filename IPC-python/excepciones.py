def divide_elemntos_de_lista(lista, divisor):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        print('ERROR, showing default numbers', e)
        return lista


lista = list(range(10))
divisor = 0

print(divide_elemntos_de_lista(lista, divisor))
