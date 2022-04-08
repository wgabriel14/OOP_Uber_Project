from car import Car


"""Aplicamos herencia"""
class UberX(Car):
    """Atributos propios de Uber X"""
    brand = str 
    model = str

    
    """Metodo constructor"""
    def __init__(self, license, driver, brand, model):
        """Se utiliza la palbra clave "super" para referinos al metodo constructor de la clase padre"""
        super.__init__(license, driver)
        self.brand = brand
        self.model = model