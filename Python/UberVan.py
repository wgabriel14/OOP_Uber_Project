from car import Car


"""Aplicamos herencia"""
class UberVan(Car):
    """Atributos propios de Uber UberVan"""    
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, license, driver, typeCarAceepted, seatsMaterial):
        super.__init__(license, driver)
        self.typeCarAccepted = typeCarAceepted
        self.seatsMaterial = seatsMaterial