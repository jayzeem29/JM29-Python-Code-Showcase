# Made by Jayzee Monserate on May 10, 2025
while True:
    try:
        def main_menu():  # defines the Main Menu of the program
            print ("\n --- Stacks and Queues Program by Jayzee Monserate ---")
            print ("-> Type '1' if you want to operate the Stack Data Structure subprogram.")
            print ("Stacks function in a last in, first out (LIFO) manner.")
            print ("-> Type '2' if you want to operate the Queue Data Structure subprogram.")
            print ("Queues function in a first in, first out (FIFO) manner.")
            print ("-> Type '3' if you want to stop running this program.")
            print ("Copyright © 2025 Jayzee Monserate. All rights reserved. \n") # \n - Line break
        main_menu() 
        array = []
        option = int(input("Type the number here: "))
        if option == 1: # Stack subprogram
            num_items = int(input("Enter the number of items that the stack array has: "))
            if num_items <= 0:
                print ("The number of items in the queue array must be a whole number greater than 0!")
            else:
                for i in range(1, num_items + 1):
                    value = input(f"Input the content of item {i} to put in the stack array: ") # Input line loops for {num_item} times
                    array.append(value) # Stores item i's content to the array
                print ("The stack array:", *array[::-1]) # prints the array in a last in, first out (LIFO) manner
                # Returns user to main menu
        elif option == 2: # Queue subprogram
            num_items = int(input("Enter the number of items that the queue array has: "))
            if num_items <= 0:
                print ("The number of items in the queue array must be a whole number greater than 0!")
            else:
                for i in range(1, num_items + 1):
                    value = input(f"Input the content of item {i} to put in the queue array: ") # Input line loops for {num_item} times
                    array.append(value) # Stores item i's content to the array
                print ("The queue array:", *array)  # prints the array in a first in, first out (FIFO) manner
                # Returns user to main menu
        elif option == 3:
            print ("END")
            break # Ends the loop that is keeping the program running (i.e. ends the program)
        else:
            print ("Please type a number between 1 to 3!")
    except ValueError: # Condition applies if the user puts a non-numeric value in the option input
    # ValueError does not crash the program because of the line above
        print ("(!)\n Error: Invalid, non-numeric input for this input! \n(!)\n")
        continue # Brings user back to the scenario input