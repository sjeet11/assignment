import re

def check_car_data(reg_num,colour):
    if not validate_car_colour(colour):
        return (False,"Invalid car colour")
    if not reg_num:
        return (False,"Car reg_num is blank")
    if not validate_reg_num(reg_num):
        return (False, "Invalid car reg_num pattern")
    return (True, "Car data is valid")

def validate_reg_num(reg_num):
    valid_car_num_format = r'[a-zA-Z]{2}-\d{2}-[a-zA-Z]{1,2}-\d{1,4}'
    return re.match(valid_car_num_format,reg_num)

def validate_car_colour(colour):
    if not colour or type(colour) != str or colour.isdigit():
        return False
    return True