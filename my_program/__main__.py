import sys
import os
import parking_slot
import car
from validate_car_data import check_car_data

    

def check_command(command, input_type = 'file'):
    '''
    Checking and running commands from command line and input file
    '''
    
    # Checking if command is empty on command line or empty line is text file
    if not command or command == "\n":
        return "Error: empty command"
    global parking_slots #setting global parking slots for future use
    commands= command.split() #converting command line arguments to list
    command_function = commands[0] #getting command function
    param_missing = "Parameter missing" #reducing repeated text

    if command_function == "create_parking_lot":
        #checking if parking slots are already created to avoid data override
        if parking_slots:
            return "Parking slot is already created"
        if len(commands)== 2:
            count = commands[1] #slot count
            if count and count.isdigit() and int(count) > 0:
                count = int(count)
                parking_slots = parking_slot.ParkingSlot(count) #creating ParkingSlot object and assigning to global variable
                return f"Created a parking lot with {count} slots"
            return "Slot count must be in digit greater than 0"
        return param_missing
    
    #all functions in ParkingSlot class
    funtion_names = [
        "park",
        "leave",
        "status",
        "slot_numbers_for_cars_with_colour",
        "slot_number_for_registration_number",
        "registration_numbers_for_cars_with_colour"
        ]

    if not command_function in funtion_names:
        return "Invalid command"

    #checking if parking slot is created
    if not parking_slots:
        return "Parking lot not created"

    if command_function == "park":
        if len(commands)== 3:
            reg_num = commands[1] #car register number
            colour = commands[2] #car colour
            response = check_car_data(reg_num, colour) #function to check data validity, returns True if data is valid else False
            if not response[0]:
                return response[1] #getting error message to know which data was incorrect
            car_data = car.Car(reg_num, colour)
            return parking_slots.park(car_data) #adding car to parking slot
        return param_missing

    if command_function == "leave":
        if len(commands)== 2:
            slot_num = commands[1] #slot number to be released for parking
            if slot_num and slot_num.isdigit():
                slot_num = int(slot_num)
                return parking_slots.leave(slot_num)
            return "Slot number must be in digit"
        return param_missing

    if command_function == "status":
        return parking_slots.status(input_type)
    if command_function == "registration_numbers_for_cars_with_colour":
        if len(commands)== 2:
            colour = commands[1]
            if colour:
                return parking_slots.registration_numbers_for_cars_with_colour(colour)
            return "Invalid colour"
        return param_missing

    if command_function == "slot_numbers_for_cars_with_colour":
        if len(commands)== 2:
            colour = commands[1]
            if colour:
                return parking_slots.slot_numbers_for_cars_with_colour(colour)
            return "Invalid colour"
        return param_missing

    if command_function == "slot_number_for_registration_number":
        if len(commands)== 2:
            reg_num = commands[1]
            if reg_num:
                return parking_slots.slot_number_for_registration_number(reg_num)
            return "Invalid car registration number"
        return param_missing
    return "Invalid command"

if __name__ == "__main__":
    args = sys.argv

    parking_slots = None
    if len(args) >= 2:
        # Input file mode
        file_inputs = args[1]
        if os.path.isfile(file_inputs):
            command_list = []
            with open(file_inputs) as fp:
                command_list = fp.readlines()
            if not command_list:
                print ("No commands found. Please check the input file")
            for command in command_list:
                print(check_command(command))

        else:
            print(f"File {file_inputs} not found")
            # Exiting with non-zero error code
            sys.exit(-1)
    else:
        # Enter the command line mode
        while(True):
            command = input("Input:\n")
            if not command:
                print("No commands found.")
                continue
            print(f'Output:\n{check_command(command,"cmd_line")}')




