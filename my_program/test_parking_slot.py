# Test
import unittest

import parking_slot
import car


class TestPark(unittest.TestCase):
    """
    Testing park method in ParkingSlot class
    """

    # Returns True if car object is instance of Car 
    def test_correct_car_object_input(self):
        """
        Test by passing correct car object with available parking slot
        """

        car_data = car.Car("KA-01-HH-1234","White") #creating car object
        slots = parking_slot.ParkingSlot(1) #creating parking slot
        response = slots.park(car_data) #adding car to slot
        self.assertEqual(response, "Allocated slot number: 1") # Returns True if car object is instance of Car 

        car_data = "carData" #not a Car object
        slots = parking_slot.ParkingSlot(1)
        response = slots.park(car_data)
        self.assertEqual(response, "Invalid car object")    # Returns True if car object is not instance of Car 

        car_data = None #None car data
        slots = parking_slot.ParkingSlot(1)
        response = slots.park(car_data)
        self.assertEqual(response, "Invalid car object")    # Returns True if car object is None

    
    # Returns True if parking slot is full 
    def test_parking_slot_full(self):
        """
        Test to check if parking slots are full
        """
        slots = parking_slot.ParkingSlot(1) #creating parkingSlot with single slot
        car_data1 = car.Car("KA-01-HH-1234","White")
        slots.park(car_data1) #assigning parking slot when slot is available
        car_data2 = car.Car("KA-01-HH-9999","White")
        response = slots.park(car_data2) #assigning parkings slot when parking is full
        self.assertEqual(response, "Sorry, parking lot is full")

    # Returns True if free slot nearest to the enrty is assigned
    def test_nearest_parking_slot(self):
        """
        Test to check if nearest empty slot is assigned
        """
        slots = parking_slot.ParkingSlot(6)
        #creating list of six cars
        cars =  [("KA-01-HH-1234","White"),
                ("KA-01-HH-9999","White"),
                ("KA-01-BB-0001","Black"),
                ("KA-01-HH-7777","Red"),
                ("KA-01-HH-2701","Blue"),
                ("KA-01-HH-3141","Black")
                ]
        for reg_num, colour in cars:
            car_data = car.Car(reg_num,colour) #creating car object
            slots.park(car_data) #adding each car using parking slots
        #clearing slot 4 and 6
        for slot_num in [4,6]:
            slots.leave(slot_num) 
        car_data2 = car.Car("KA-01-HH-9999","White")
        response = slots.park(car_data2) #adding car to empty slot
        self.assertEqual(response, "Allocated slot number: 4") #expecting nearest slot number 4 to be allocated



class TestLeave(unittest.TestCase):
    """
    Testing 'leave' method in ParkingSlot class
    """
    def setUp(self):
        """
        creating parking slot to check leave method
        """
        slots = parking_slot.ParkingSlot(6)
        #creating list of three cars
        cars =  [("KA-01-HH-1234","White"),
                ("KA-01-HH-9999","White"),
                ("KA-01-BB-0001","Black"),
                ]
        for reg_num, colour in cars:
            car_data = car.Car(reg_num,colour) #creating car object
            slots.park(car_data) #adding each car using parking slots
        self.parkingSlot = slots


    def test_correct_input(self):
        """
        Test to check input type
        """

        response = self.parkingSlot.leave(1) #passing int
        self.assertEqual(response, "Slot number 1 is free") # Returns True if car object is instance of Car 

        response = self.parkingSlot.leave(1.5) #passing float
        self.assertEqual(response, "Invalid slot number, provide integer greater than 0") 

        response = self.parkingSlot.leave("") #passing empty string
        self.assertEqual(response, "Invalid slot number, provide integer greater than 0") 

        response = self.parkingSlot.leave("1") #passing string containg int
        self.assertEqual(response, "Invalid slot number, provide integer greater than 0") 

        response = self.parkingSlot.leave(-1) #passing negetive value
        self.assertEqual(response, "Invalid slot number, provide integer greater than 0") 


    def test_leave_on_empty_slot(self):
        """
        Test to check leave method on empty slot
        """
        self.parkingSlot.leave(1) #clearing slot 1
        response = self.parkingSlot.leave(1) #clearing slot 1 again
        self.assertEqual(response, "No car has been allocated in slot number 1")# true is slot is already empty


class TestRegistrationNumbersForCarsWithColour(unittest.TestCase):
    """
    Testing 'registration_numbers_for_cars_with_colour' method in ParkingSlot class
    """
    def setUp(self):
        """
        creating parking slot to check method
        """
        slots = parking_slot.ParkingSlot(6)
        #creating list of six cars
        cars =  [("KA-01-HH-1234","White"),
                ("KA-01-HH-9999","White"),
                ("KA-01-BB-0001","Black"),
                ("KA-01-HH-7777","Red"),
                ("KA-01-HH-2701","Blue"),
                ("KA-01-HH-3141","Black")
                ]
        for reg_num, colour in cars:
            car_data = car.Car(reg_num,colour) #creating car object
            slots.park(car_data) #adding each car using parking slots
        self.parkingSlot = slots


    def test_input(self):
        response = self.parkingSlot.registration_numbers_for_cars_with_colour("White") #valid colour
        self.assertEqual(response, "KA-01-HH-1234, KA-01-HH-9999")

        response = self.parkingSlot.registration_numbers_for_cars_with_colour("white") #case sensitivity check
        self.assertEqual(response, "KA-01-HH-1234, KA-01-HH-9999")

        response = self.parkingSlot.registration_numbers_for_cars_with_colour("Green") #unavailable colour
        self.assertEqual(response, "Sorry, no Green colour cars are parked")
        
        response = self.parkingSlot.registration_numbers_for_cars_with_colour("") #empty string
        self.assertEqual(response, "Colour cannot be empty")

class TestSlotNumbersForCarsWithColour(unittest.TestCase):
    """
    Testing 'slot_numbers_for_cars_with_colour' method in ParkingSlot class
    """
    def setUp(self):
        """
        creating parking slot to check method
        """
        slots = parking_slot.ParkingSlot(6)
        #creating list of six cars
        cars =  [("KA-01-HH-1234","White"),
                ("KA-01-HH-9999","White"),
                ("KA-01-BB-0001","Black"),
                ("KA-01-HH-7777","Red"),
                ("KA-01-HH-2701","Blue"),
                ("KA-01-HH-3141","Black")
                ]
        for reg_num, colour in cars:
            car_data = car.Car(reg_num,colour) #creating car object
            slots.park(car_data) #adding each car using parking slots
        self.parkingSlot = slots


    def test_input(self):
        response = self.parkingSlot.slot_numbers_for_cars_with_colour("White") #valid colour
        self.assertEqual(response, "1, 2")

        response = self.parkingSlot.slot_numbers_for_cars_with_colour("white") #case sensitivity check
        self.assertEqual(response, "1, 2")

        response = self.parkingSlot.slot_numbers_for_cars_with_colour("Green") #unavailable colour
        self.assertEqual(response, "Sorry, no Green colour cars are parked")
        
        response = self.parkingSlot.slot_numbers_for_cars_with_colour("") #empty string
        self.assertEqual(response, "Colour cannot be empty")


class TestSlotNumberForRegistrationNumber(unittest.TestCase):
    """
    Testing 'slot_number_for_registration_number' method in ParkingSlot class
    """
    def setUp(self):
        """
        creating parking slot to check method
        """
        slots = parking_slot.ParkingSlot(6)
        #creating list of six cars
        cars =  [("KA-01-HH-1234","White"),
                ("KA-01-HH-9999","White"),
                ("KA-01-BB-0001","Black"),
                ("KA-01-HH-7777","Red"),
                ("KA-01-HH-2701","Blue"),
                ("KA-01-HH-3141","Black")
                ]
        for reg_num, colour in cars:
            car_data = car.Car(reg_num,colour) #creating car object
            slots.park(car_data) #adding each car using parking slots
        self.parkingSlot = slots


    def test_input(self):
        response = self.parkingSlot.slot_number_for_registration_number("KA-01-HH-1234") #registration number of parked car
        self.assertEqual(response, 1) #car parked at slot 1

        response = self.parkingSlot.slot_number_for_registration_number("KA-01-HH-1236") #registration number of parked not car
        self.assertEqual(response, "Not found") # car not found in parking lot

        response = self.parkingSlot.slot_number_for_registration_number("KA-01-HH") #Invalid registration number
        self.assertEqual(response, "Invalid car reg_num pattern")
        
        response = self.parkingSlot.slot_number_for_registration_number("") #empty string
        self.assertEqual(response, "reg_num cannot be empty")

if __name__ == '__main__':
    unittest.main()