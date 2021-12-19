# Test
import unittest

import car


class TestCar(unittest.TestCase):
    """
    Testing create car
    """

    def test_input(self):
        """
        Test by passing different car arguments
        """

        car_data = car.Car("KA-01-HH-1234","White") #passing correct data
        self.assertEqual(str(car_data), "KA-01-HH-1234 White") # Returns True if car data arguments are correct

        with self.assertRaises(ValueError):
            car_data = car.Car("KA-01-HH-AAA","White")#passing incorrect register number pattern

            car_data = car.Car("","")#passing empty arguments
        
            car_data = car.Car()#passing no arguments

            car_data = car.Car("KA-01-HH-AAA",1) #incorrect car colour
        
        car_data = car.Car("ka-01-hh-1234","white") #passing lowercase data
        self.assertEqual(str(car_data), "KA-01-HH-1234 White")#data gets corrected

        car_data = car.Car("ka-01-hh-1234","WHITE") #passing uppercase colour
        self.assertEqual(str(car_data), "KA-01-HH-1234 White") #colour case gets corrected

if __name__ == '__main__':
    unittest.main()