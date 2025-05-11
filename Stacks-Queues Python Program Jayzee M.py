# Made by Jayzee Monserate on May 11, 2025
array = []  # Declares array for both Stack and Queue subprograms 
 # --- USER INTERFACE DEFINITIONS ---
def main_menu():  # defines the Main Menu of the program
    print("\n --- Stacks and Queues Program by Jayzee Monserate ---")
    print("-> Type '1' if you want to operate the Stack Data Structure subprogram.")
    print("Stacks function in a last in, first out (LIFO) manner.")
    print("-> Type '2' if you want to operate the Queue Data Structure subprogram.")
    print("Queues function in a first in, first out (FIFO) manner.")
    print("-> Type '3' if you want to stop running this program.")
    print("Copyright © 2025 Jayzee Monserate. All rights reserved. \n")

def stack_subprogram():  # defines the Stack Subprogram of the program
    num_items = int(input("Enter the number of items that the stack array has: "))
    if num_items <= 0:
        print("The number of items in the stack array must be a whole number greater than 0!")
    else:
        print(f"You requested to insert {num_items} items to the stack array. To go back to the main menu, type '!EXIT!'.")
        print("To delete the last item entered in the stack array, type 'BACK1'. \n")
        i = 0
        while i < num_items:
            value = input(f"Input the content of item {i + 1} to put in the stack array: ")
            if value.upper() == "!EXIT!":
                return # redirects user to Main Menu
            elif value.upper() == "BACK1":
                if i > 0:
                    i -= 1  # Goes to the last item
                    array.pop()  # Removes the last item entered from the stack array
                    print(f"Item removed. Going back to item {i + 1}...")  # Previous item number
                    continue  # i decrease by 1
                else:
                    print("You are at the first item right now; you cannot go back further!")
                    continue  # Keeps user in the first item
            else:
                array.append(value)  # Store item in the array
                i += 1  # Goes to the next item
        print("The stack array contains:", *array[::-1])
        array.clear()

def queue_subprogram():  # defines the Queue Subprogram of the program
    num_items = int(input("Enter the number of items that the queue array has: "))
    if num_items <= 0:
        print("The number of items in the queue array must be a whole number greater than 0!")
    else:
        print(f"You requested to insert {num_items} items to the queue array. To go back to the main menu, type '!EXIT!'.")
        print("To delete the first item in the queue array, type 'BACK1' \n.")
        i = 0
        while i < num_items:
            value = input(f"Input the content of item {i + 1} to put in the queue array: ")
            if value.upper() == "!EXIT!":
                return # redirects user to Main Menu
            elif value.upper() == "BACK1":
                if i > 0:
                    i -= 1  # Goes to the last item
                    array.pop(0)  # Removes the leftmost item in the array (FIFO)
                    print(f"Item removed. Going back to item {i}...") 
                    continue # i decrease by 1
                else:
                    print("You are at the first item right now; you cannot go back further!")
                    continue  # Keeps user in the first item
            else:
                array.append(value)  # Store item in the array
                i += 1  # Goes to the next item
        print("The queue array contains:", *array)
        array.clear()

# --- CODE TO LOAD THE USER INTERFACES ---
while True:
    try:
        main_menu()
        option = int(input("Type the number here: "))
        if option == 1:  # Redirects user to Stack subprogram
            stack_subprogram()
        elif option == 2:  # Redirects user to Queue subprogram
            queue_subprogram()
        elif option == 3:
            print("END")
            break  # Ends the loop that is keeping the program running (i.e. ends the program)
        else:
            print("Please type a number between 1 to 3!")

    except ValueError:  # Condition applies if the user puts a non-numeric value in the option input
        print("(!)\n Error: Invalid, non-numeric input for the option selection input! \n(!)\n")