"""
En python debemos empezar importando el elemento
"""
from car import Car

if __name__ == "__main__":
    print("Hola mundo!")
    
    car = Car()
    car.license = "VZLA123"
    car.driver = "Williams Reyes"
    print(vars(car))

    car2 = Car()
    car2.license = "USB1234"
    car2.driver = "Elon Musk"
    print(vars(car2))

    