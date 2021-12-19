Parking slot program
==============================

What Is This?
-------------

This is a Python application to create a parking lot automated ticketing system.
Parking lot is assigned with the 'n' number of slots.
Each slot is given a number starting at 1 increasing with increasing distance from the entry point in steps of one.
When a car enters the parking lot, a slot is assigned to the car, this process includes storing registration number (number plate) and the colour of the car and allocating an available parking slot to the car.
Empty parking slot nearest to the entry is allocated to car. 
At the exit slot is again made available.
Also has function to find:
a) Registration numbers of all cars of a colour.
b) Slot number in which a car with a given registration number is parked.
c) Slot numbers of all slots where a car of a colour is parked.



How To Use This
---------------

Navigate to current repository path

There are two ways to use the application

a) Using command line arguments
    Command to run:
    
```bash
$python3 my_program
Input:
create_parking_lot 6
Output:
Created a parking lot with 6 slots
Input:
park KA-01-HH-1234 White
Output:
Allocated slot number: 1
Input:
park KA-01-HH-9999 White
Output:
Allocated slot number: 2
Input:
park KA-01-BB-0001 Black
Output:
Allocated slot number: 3
Input:
park KA-01-HH-7777 Red
Output:
Allocated slot number: 4
Input:
park KA-01-HH-2701 Blue
Output:
Allocated slot number: 5
Input:
park KA-01-HH-3141 Black
Output:
Allocated slot number: 6
Input:
leave 4
Output:
Slot number 4 is free
Input:
status
Output
Slot No.
Registration No

Colour
1
KA-01-HH-1234
White
2
KA-01-HH-9999
White
3
KA-01-BB-0001
Black
5
KA-01-HH-2701
Blue
6
KA-01-HH-3141
Black
Input:
park KA-01-P-333 White
Output:
Allocated slot number: 4
Input:
park DL-12-AA-9999 White
Output:
Sorry, parking lot is full
Input:
registration_numbers_for_cars_with_colour White
Output:
KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
Input:
slot_numbers_for_cars_with_colour White
Output:
1, 2, 4
Input:
slot_number_for_registration_number KA-01-HH-3141
Output:
6
Input:
slot_number_for_registration_number MH-04-AY-1111
Output:
Not found
```

 b) Passing commands stored in a text file
 
    create a text file in repository path.
    Add commands to check the application.
    
    Sample Input file commands (file_inputs.txt):
    
      create_parking_lot 6
      park KA-01-HH-1234 White
      park KA-01-HH-9999 White
      park KA-01-BB-0001 Black
      park KA-01-HH-7777 Red
      park KA-01-HH-2701 Blue
      park KA-01-HH-3141 Black
      leave 4
      status
      park KA-01-P-333 White
      park DL-12-AA-9999 White
      registration_numbers_for_cars_with_colour White
      slot_numbers_for_cars_with_colour White
      slot_number_for_registration_number KA-01-HH-3141
      slot_number_for_registration_number MH-04-AY-1111

    Command to run:
```bash
$ python3 my_program file_inputs.txt > file_output.txt
```
    
    Expected Output (to console, newline after every output)- file_output.txt:
    
        Created a parking lot with 6 slots
        Allocated slot number: 1
        Allocated slot number: 2
        Allocated slot number: 3
        Allocated slot number: 4
        Allocated slot number: 5
        Allocated slot number: 6
        Slot number 4 is free
        Slot No. Registration No Colour
        1 KA-01-HH-1234 White
        2 KA-01-HH-9999 White
        3 KA-01-BB-0001 Black
        5 KA-01-HH-2701 Blue
        6 KA-01-HH-3141 Black
        Allocated slot number: 4
        Sorry, parking lot is full
        KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
        1, 2, 4
        6
        Not found






