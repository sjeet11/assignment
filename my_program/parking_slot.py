from car import Car

from validate_car_data import validate_reg_num

class ParkingSlot(object):
    """
    Class for parking related functionality
    """
    def __init__(self,count):
        self.count = count
        self.parked_cars = dict.fromkeys(range(1,count+1))


    def __str__(self):
        return f"Created a parking lot with {self.count} slots"


    def park(self,car):
        if isinstance(car, Car):
            if self.count == 0:
                return "Sorry, parking lot is full"
            all_empty_slots = dict(filter(lambda value:value[1] == None, self.parked_cars.items()))
            empty_slot_num = list(all_empty_slots.keys() )   
            empty_slot_num.sort()
            nearest_empty_slot = empty_slot_num[0]
            self.parked_cars[nearest_empty_slot] = car
            self.count -= 1
            return f"Allocated slot number: {nearest_empty_slot}"
        return "Invalid car object"

    def __used_slots(self):
        return dict(filter(lambda value:(value[1] != None), self.parked_cars.items()))


    def leave(self,slot_num):
        if not slot_num in self.parked_cars.keys():
            return "Invalid slot number, provide integer greater than 0"
        if self.parked_cars.get(slot_num) == None:
            return f"No car has been allocated in slot number {slot_num}"
        self.parked_cars[slot_num] = None
        self.count += 1
        return f"Slot number {slot_num} is free"

    def __slot_data_for_cars_with_colour(self, colour):
        used_slots = self.__used_slots()
        if used_slots:
            colour_slot_data = dict(filter(lambda value:(value[1].colour == str(colour).capitalize()), used_slots.items()))
            return colour_slot_data
        return


    def slot_numbers_for_cars_with_colour(self, colour):
        if not colour:
            return "Colour cannot be empty"
        colour_slots = self.__slot_data_for_cars_with_colour(colour)
        if (not colour_slots):
            return f"Sorry, no {colour} colour cars are parked"
        return f"{str(list(colour_slots.keys()))[1:-1]}"


    def registration_numbers_for_cars_with_colour(self, colour):
        if not colour:
            return "Colour cannot be empty"
        colour_slots = self.__slot_data_for_cars_with_colour(colour)
        if (not colour_slots):
            return f"Sorry, no {colour} colour cars are parked"
        car_reg_num = [car.reg_num for car in colour_slots.values() ]
        
        return f"{(', ').join(car_reg_num)}"


    def slot_number_for_registration_number(self, reg_num):
        if not reg_num:
            return "reg_num cannot be empty"
        if not validate_reg_num(reg_num):
            return "Invalid car reg_num pattern"
        used_slots = self.__used_slots()
        if used_slots:
            car_num_slot = dict(filter(lambda value:(value[1].reg_num == str(reg_num).upper()), used_slots.items()))
            if car_num_slot:
                return list(car_num_slot.keys())[0]
        return "Not found"


    def status(self, input_type):
        used_slots = self.__used_slots()
        if used_slots:
            response = ''
            delimiter = '    ' if input_type == "file" else "\n"
            response = delimiter.join(["Slot No.", "Registration No", "Colour"])
            for slot_num, car_data in used_slots.items():
                new_line = delimiter.join([str(slot_num), car_data.reg_num, car_data.colour])
                response +=f"\n{new_line}"
            return response
        return "No car parked"

