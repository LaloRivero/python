# -*- coding: utf-8 -*-
countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(raw_input('Escribe el nombre de un país: ')).lower()
    try:
        print('La población de {} es: {} millones'.format(
            country, contries[country]))
    except KeyError:
        print('Lo siento no tenemos el dato de la población de {}'.format(country))
