from account import Account


class Car:
    id = int
    license = str
    driver = Account(" ", " ")
    passenger_count = int

    def __init__(self, license=str, driver=str, ):
        self.license = license
        self.driver = driver
