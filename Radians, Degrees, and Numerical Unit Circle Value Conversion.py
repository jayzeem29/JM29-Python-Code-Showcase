import math # Made by Jayzee Monserate, May 8, 2025
# \n in a string - line break
def main_menu(): # Main Menu
    print ("\n Radians-Degrees Program made by Jayzee Monserate")
    print ("-> Type '1' if you want to do a radian to degree conversion.")
    print ("-> Type '2' if you want to do a degree to radian conversion.")
    print ("-> Type '3' if you want to convert a degree or radian to a numerical value using one of these trig functions:")
    print (" * the sine function \n * the cosine function \n * the tangent function")
    print (" * the cosecant function \n * the secant function \n * the cotangent function")
    print ("-> Type '4' if you stop running this program.")
    print ("Copyright © 2025 Jayzee M. All rights reserved. \n")
while True:
    main_menu()
    try:
        scenario = int(input("Type the number here: "))
        if scenario == 1: # SCENARIO 1 - Radians to Degrees Conversion
            radians = float(input("Enter the angle in radians: "))
            degrees = math.degrees(radians)
            print ("\n OUTPUT:")
            print (f"{radians} radians is equal to {degrees} degrees. \n")
            # when prints are completed, program returns user to Main Menu
        elif scenario == 2: # SCENARIO 2 - Degrees to Radians Conversion
            degrees = float(input("Enter the angle in degrees: "))
            radians = math.radians(degrees)
            print ("\n OUTPUT:")
            print (f"{degrees} degrees is equal to {radians} radians. \n")
            # when prints are completed, program returns user to Main Menu
        elif scenario == 3: # SCENARIO 3 - Degrees/Radians to Numerical Value in Unit Circle Conversion
            print("If your angle is in radians, type '1'. If your angle is in degrees, type '2'.")
            rad_or_deg = int(input("Type the number here: "))
            if rad_or_deg == 1:
                angle = float(input("Enter the angle in radians: "))
            elif rad_or_deg == 2:
                angle = math.radians(float(input("Enter the angle in degrees: ")))
            # Python does not do trig functions by degrees, so the math.radians function is necessary for 
            # the 'angle' variable if rad_or_deg == 2
            else:
                print ("Please type either '1' or '2'!")
                continue # returns user to Main Menu
            print ("Choose the following and type the number:")
            print (" *'1' for sine \n *'2' for cosine \n *'3' for tangent")
            print (" *'4' for cosecant \n *'5' for secant \n *'6' for cotangent \n")
            sub_scenario = int(input("Type the number here: "))
            if sub_scenario == 1:
                trig_function = "sine"
                trig_value = math.sin(angle)
            elif sub_scenario == 2:
                trig_function = "cosine"
                trig_value = math.cos(angle)
            elif sub_scenario == 3:
                trig_function = "tangent"
                trig_value = math.tan(angle)
            elif sub_scenario == 4:
                trig_function = "cosecant"
                trig_value = (1 / math.sin(angle))
            elif sub_scenario == 5:
                trig_function = "secant"
                trig_value = (1 / math.cos(angle))
            elif sub_scenario == 6:
                trig_function = "cotangent"
                trig_value = (1 / math.tan(angle))
            else:
                print ("Please enter a number between 1 to 6!")
                continue # returns user to Main Menu
            print ("\n OUTPUT:")
            if rad_or_deg == 1:
                print (f"The {trig_function} value of {angle} radians is {trig_value} \n")
            else:
                print (f"The {trig_function} value of {math.degrees(angle)} degrees is {trig_value} \n")
            # To return variable 'angle' in degrees, math.degrees is necessary
            # when prints are completed, program returns user to Main Menu
        elif scenario == 4: # Allows user to quit the program while running it
            print ("END")
            break # ends the loop and program
        else:
            print ("Please input a number between 1 to 4!")
    except ValueError: # Condition applies if the user puts a non-numeric value in a float input
    # ValueError does not crash the program in the line above
        print ("(!)\n Error: Invalid, non-numeric input! \n(!)\n")
        continue # Brings user back to the scenario input
    except ZeroDivisionError: # for undefined angles in Scenario 3
        print ("\n OUTPUT:")
        print ("undefined")
        continue 
