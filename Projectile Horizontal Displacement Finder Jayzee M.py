# --- SUBPROGRAM CODE ---
import math
def main_menu():
    print ("--- Projectile Horizontal Displacement Calculator by Jayzee Monserate ---")
    print ("-> Type '1' if the projectile's take-off height is the same as it's landing height.")
    print ("-> Type '2' if the projectile's take-off height is higher than it's landing height.")
    print ("-> Type '3' if the projectile's take-off height is lower than it's landing height.")
    print ("-> Type '4' if you want to stop running this program.")
    print ("Copyright © 2025 Jayzee Monserate. All rights reserved. \n")

def back_main_menu():
    print ("To go back to the Main Menu, type a non-numeric input. \n")

def upward_half(): # "Upward Half" of the projectile's parabolic path
    velocity_takeoff = float(input("Enter the projectile's take-off velocity in metres per second: ")) # Take-Off Velocity
    degrees_or_radians = input("If your take-off angle is in degrees, type 'X', if it is in radians, type something else: ")
    if degrees_or_radians.strip().upper() == "X":
        angle_takeoff = math.radians(float(input("Enter the projectile's take-off angle in degrees: ")))
    else:
        angle_takeoff = float(input("Enter the projectile's take-off angle in radians: "))
    velocity_x = velocity_takeoff * math.cos(angle_takeoff) # Horizontal Velocity Component
    velocity_up = velocity_takeoff * math.sin(angle_takeoff) # Vertical Velocity Component
    print (f"The take-off velocity's horizontal and vertical components are {velocity_x:.2f} and {velocity_up:.2f} metres, respectively.")
    time_up = abs(velocity_up / 9.81) # vf = vo + at -> -vo / -9.81t -> Time projectile is up in the air
    print (f"The time for the projectile to go from it's take-off spot to it's vertical apex is {time_up:.2f} seconds.")
    return velocity_x, velocity_up, time_up
    # Returns all three variables above to use for later functions in the program

def takeoff_equal_landing(velocity_x, velocity_up, time_up): # "Landing Half" of the projectile's parabolic path where take-off height == landing height
    displacement_x = (velocity_x) * (time_up * 2)
    # horizontal displacement = take-off velocity horizontal component * (time up + time down)
    # Time up equals time down where projectile take-off height is the same as the landing height
    print (f"The projectile landed in the ground with a vertical velocity of -{velocity_up:.2f} metres per second downwards.")
    # Vertical Take-Off Velocity = Vertical Landing Velocity where take-off height == landing height for projectiles
    print (f"The horizontal displacement of the projectile is {displacement_x:.2f} metres.")
    # --- End of Option 1 shown below in the "CODE TO LOAD SUBPROGRAMS AND LOOP CODE" section --- 

def upwards_displacement(velocity_up):
    displacement_up = (velocity_up ** 2) / 19.62
    print (f"The projectile goes {displacement_up:.2f} metres upwards from it's take-off spot to it's vertical apex. \n")
    return displacement_up 
    # Returns the displacement_up variable to use for the downwards_displacement_takeoff_lower_landing/downwards_displacement_takeoff_higher_landing function

def downwards_displacement_takeoff_lower_landing(displacement_up): # Used where projectile takeoff height is lower than it's landing height
    height_difference = float(input("Enter how many metres lower is the take-off spot's height is compared to the landing spot's height: "))
    displacement_down = -(displacement_up - height_difference) 
    print (f"The projectile goes {displacement_down:.2f} metres downwards from it's vertical apex to it's landing spot.")
    return displacement_down
    # Returns the displacement_down variable to use for the takeoff_not_equal_landing function

def downwards_displacement_takeoff_higher_landing(displacement_up): # Used where projectile takeoff height is higher than it's landing height
    height_difference = float(input("Enter how many metres higher is the take-off spot's height is compared to the landing spot's height: "))
    displacement_down = -(displacement_up + height_difference)
    print (f"The projectile goes {displacement_down:.2f} metres downwards from it's vertical apex to it's landing spot.")
    return displacement_down
    # Returns the displacement_down variable to use for the takeoff_not_equal_landing function

def takeoff_not_equal_landing(displacement_down, velocity_x, time_up): # "Landing Half" of the projectile's parabolic path where landing height != take-off height
    time_down = math.sqrt(displacement_down/-4.905) # d = vo * t + 1/2a * t^2 -> d = -4.905t^2
    print (f"The time for the projectile to go from it's vertical apex to it's landing spot is {time_down:.2f} seconds.")
    velocity_down = -9.81 * time_down # vf = vo + at -> vf = -9.81 * time_down
    print (f"The projectile landed in the ground with a vertical velocity of {velocity_down:.2f} metres per second downwards.")
    displacement_x = velocity_x * (time_up + time_down) 
    # horizontal displacement = take-off velocity horizontal component * (time up + time down)
    print (f"The horizontal displacement of the projectile is {displacement_x:.2f} metres. \n")
    # --- End of Options 2 and 3 shown below in the "CODE TO LOAD SUBPROGRAMS AND LOOP CODE" section ---


# --- CODE TO LOAD SUBPROGRAMS AND LOOP CODE---
while True:
    try:
        main_menu()
        option = float(input("Select your option by typing the number here: "))
        if option == 1:
            print ("--- Projectile Takeoff Height = Projectile Landing Height ---")
            back_main_menu()
            velocity_x, velocity_up, time_up = upward_half()
            takeoff_equal_landing(velocity_x, velocity_up, time_up)
        elif option == 2:
            print ("--- Projectile Takeoff Height > Projectile Landing Height ---")
            back_main_menu()
            velocity_x, velocity_up, time_up = upward_half()
            displacement_up = upwards_displacement(velocity_up)
            displacement_down = downwards_displacement_takeoff_higher_landing(displacement_up)
            takeoff_not_equal_landing(displacement_down, velocity_x, time_up)
        elif option == 3:
            print ("--- Projectile Takeoff Height < Projectile Landing Height ---")
            back_main_menu()
            velocity_x, velocity_up, time_up = upward_half()
            displacement_up = upwards_displacement(velocity_up)
            displacement_down = downwards_displacement_takeoff_lower_landing(displacement_up)
            takeoff_not_equal_landing(displacement_down, velocity_x, time_up)
        elif option == 4:
            print ("END")
            break # Ends the loop and program
        else:
            print ("Please type a whole number between 1 to 4!")
    except ValueError:
        print("Input error! That input needed to be a number!")