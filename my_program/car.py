from validate_car_data import validate_car_colour, validate_reg_num #import function to check input data


class Car:
    """
    Car class which will store car attributes
    """
    
    def __init__(self, reg_num, colour):
        
        self.reg_num = str(reg_num).upper() #car registration number
        self.colour = str(colour).capitalize() #car colour


    @property
    def reg_num(self):
        return self._reg_num


    @reg_num.setter
    def reg_num(self, value):
        if not validate_reg_num(value):
            raise ValueError("Incorrect car register number pattern")
        self._reg_num = value


    @property
    def colour(self):
        return self._colour


    @colour.setter
    def colour(self, value):
        if not validate_car_colour(value):
            raise ValueError("Incorrect car colour")
        self._colour = value


    def __str__(self):
        return f'{self.reg_num} {self.colour}'
