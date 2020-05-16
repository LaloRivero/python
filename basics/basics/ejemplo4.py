# -*- coding:utf-8 -*-


def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97
    return ammount * mex_to_col_rate


def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos Mexicanos a pesos Colombianos')
    print('')

    ammount = float(
        raw_input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))
    result = foreign_exchange_calculator(ammount)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))


if __name__ == '__main__':
    run()
