##!/usr/bin/env python
__author__ = "Alex Pujols"
__copyright__ = "Copyright 2020, proceedural problems examples TIM-6110 wk2"
__credits__ = ["Alex Pujols"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Alex Pujols"
__email__ = "alex.pujols@gmail.com"
__status__ = "Prototype"

# Import modules declarations

# Function declarations

# Function #1
def input_validate():
    while True:
        try:
            validate = int(input(": "))
            break
        except:
            print ("Incorrect value! Please make a new selection")
    return validate
# Function #2
def filter(predicate, values):
    if (predicate == 1):
        odd_number_list = []
        for number in values:
            if number % 2 != 0:
                odd_number_list.append(number)
        values = odd_number_list
        return values
    else:
        print ("Wrong value entered! Going back to main menu")
        return values
# Function #3
def explode(predicate, string):
    if (predicate == 1):
        new_string = ''.join([j for i, j in enumerate(string) if j not in string[:i]])
        string = new_string
        return string
    else:
        print ("Wrong value entered! Going back to main menu")
        return string
# Function #4
def implode(predicate, string):
    if (predicate == 1):
        new_string = ''.join(string)
        return new_string
    else:
        print ("Wrong value entered! Going back to main menu")
        return values
# Function #5
def tribble_calculator(number_of_hours):
    reproduction_cycles = int(number_of_hours / 12)
    #current_number_of_tribbles = int((reproduction_cycles * 10) * current_number_of_tribbles)
    final_number_of_tribbles = int(11 ** reproduction_cycles)
    days = int(number_of_hours / 24)
    print (f"\nAfter {number_of_hours} hours (ie. {days} days), the number of Tribbles would have multiplied to {final_number_of_tribbles}\n")
    return number_of_hours
# Main code begins
print ("\n")

# Set globals

while True:
#    print ("\n")
    print ("Hi, which function would you like to run?")
    print ("1 - Filter function")
    print ("2 - Explode funtion")
    print ("3 - Implode function")
    print ("4 - Problem-solving function")
    print ("0 - EXIT")

    # Take user input and validate
    selection = input_validate()

    #If user selects main option 1
    if (selection == 1):
        print ("\nYou selected the filter function!\n")
        # Select sub-type item
        print ("Which function filter would you like to apply?")
        print ("1 - Odd filter")
        sub_selection = input_validate()
        # If user selects sub-type 1
        if (sub_selection == 1):
            arr = []
            print("\nYou selected the odd filter!\n")
            number_of_elements = int(input("Enter number of elements: "))
            print("Please type each number then hit 'enter'")
            for i in range(0, number_of_elements):
                element = int(input())
                arr.append(element)
            print(f"\nYou entered {arr}\n")
            new_arr = filter(1, arr)
            print(f"The odd numbers are: {new_arr} \n")
    #If user selects main option 2
    if (selection == 2):
        print ("\nYou selected the explode function!\n")
        # Select sub-type item
        print ("Which explode function would you like to apply?")
        print ("1 - Exploder")
        sub_selection = input_validate()
        # If user selects sub-type 1
        if (sub_selection == 1):
            arr = []
            i = 0
            print("\nYou selected the exploder!\n")
            arr = str(input("Please type the word: "))
            print(f"\nYou entered: {arr}\n")
            new_arr = explode(1, arr)
            print("The exploded word (minus duplicates)is: ", end = "")
            # Display string character by character with proper spacing
            while i < len(new_arr):
                print (f"{new_arr[i]}  ", end = "")
                i += 1
            print("\n")
        #If user selects main option 3
    if (selection == 3):
        print ("\nYou selected the implode function!\n")
        # Select sub-type item
        print ("Which implode function would you like to apply?")
        print ("1 - Imploader")
        sub_selection = input_validate()
        # If user selects sub-type 1
        if (sub_selection == 1):
            arr = []
            print("\nYou selected the imploder!\n")
            number_of_characters = int(input("Enter number of characters: "))
            print("\nPlease type each character then hit 'enter'")
            for i in range(0, number_of_characters):
                element = str(input())
                arr.append(element)
            new_arr = implode(1, arr)
            print(f"\nYou entered: {new_arr}\n")
        #If user selects main option 4
    if (selection == 4):
        print ("\nYou selected the problem-solving function!\n")
        # Select sub-type item
        print ("What type of problem-solving function would you like to apply?")
        print ("1 - Counting Tribbles! \n")
        sub_selection = input_validate()
        # If user selects sub-type 1
        if (sub_selection == 1):
            print ("\nLet's estimate tribbles! Enter the number of hours in the future would you like to estimate")
            number_of_hours = input_validate()
            tribble_calculator(number_of_hours)
    #If user selects exit
    if (selection == 0):
        print ("\n You have chosen to leave the program.  Goodbye! \n")
        break
