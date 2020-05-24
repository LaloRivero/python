
def exhaustive(objective):
    answer = 0
    cont = 0
    while answer ** 2 < objective:
        answer += 1
        cont += 1
    if answer**2 == objective:
        print(
            f'The square root of {objective} is {answer}. Number of iterations: {cont}')
    else:
        print(f'{objective} does not have a exact square root')


def approach(objective, epsilon):
    step = epsilon**2
    answer = 0.0
    cont = 0

    while abs(answer**2 - objective) >= epsilon and answer <= objective:
        answer += step
        cont += 1

    if abs(answer**2 - objective) >= epsilon:
        print(f"Sorry the square root of {objective} can't be found", cont)
    else:
        print(
            f'The square root of {objective} is {answer}. Number of iterations: {cont}')


def binary_search(objective, epsilon):
    low = 0.0
    high = max(1.0, objective)
    answer = (high + low)/2
    cont = 0

    while abs(answer**2 - objective) >= epsilon:
        if answer**2 < objective:
            low = answer
        else:
            high = answer
        answer = (high+low)/2
        cont += 1

    print(
        f'The square root of {objective} is {answer}. Number of iterations: {cont}')


if __name__ == "__main__":
    option = input('''
          Select the function that you want to use:

          [e]xhaustive enumeration
          [a]pproach
          [b]inary search

          ''')

    if option == 'e':
        objective = int(input('Please type a number: '))
        exhaustive(objective)

    elif option == 'a':
        objective = int(input('Please type a number: '))
        epsilon = float(input('Please type your tolerance (epsilon): '))
        approach(objective, epsilon)

    elif option == 'b':
        objective = int(input('Please type a number: '))
        epsilon = float(input('Please type your tolerance (epsilon): '))
        binary_search(objective, epsilon)

    else:
        print('Sorry, incorrect option please try again')
