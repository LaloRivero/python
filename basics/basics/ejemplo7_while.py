# -*- coding: utf-8 -*-
import random


def run():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(raw_input('Try a number: '))

        if(number == random_number):
            print('Congrats. You find the right number')
            number_found = True
        elif number > random_number:
            print('The number has a small value')
        else:
            print('The number has a bigger value')


if __name__ == '__main__':
    run()
