from car import Car


"""Aplicamos herencia"""
class UberBlack(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, license, driver, typeCarAceepted, seatsMaterial):
        super.__init__(license, driver)
        self.typeCarAccepted = typeCarAceepted
        self.seatsMaterial = seatsMaterial