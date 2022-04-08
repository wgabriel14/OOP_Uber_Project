from account import Account

class Car:
    id = int
    license = str
    driver = Account("","") # Recordar que driver hereda de Account, por eso el cambio
    passegenger = int

    def __init__(self, license, driver):
        self.license  = license
        self.driver   = driver