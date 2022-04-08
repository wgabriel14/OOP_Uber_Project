"""
En python debemos empezar importando el elemento
"""
from account import Account
from car import Car

if __name__ == "__main__":
    print("Hola mundo!")
    
    car = Car("VZLA123", Account("Williams Reyes", "CI123"))
    print(vars(car))
    print(vars(car.driver))

    car2 = Car("USB1234", Account("Elon Musk", "USB1234"))
    print(vars(car2))
    print(vars(car2.driver))

    