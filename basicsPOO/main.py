from car import Car
from account import Account

if __name__ == "__main__":
    car = Car("ENA8987", Account("Sergio Bernal", "SAD23423dsASFDE"))
    print(vars(car))
    print(vars(car.driver))
