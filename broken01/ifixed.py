#!/usr/bin/env python
# a program that prompts a user for two operators and and operation (plus or minus)
# the program then shows the result.
# the user may enter q to exit the program.

calc1 = 0.0
calc2 = 0.0
operation =""

while (calc1 !=  "q"): # needs fixing
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = raw_input() 
    if calc1.lower == "q": # might need space
        break
    calc1 = float(calc1) # might need to be sooner
    print("\nWhat is the second operator? Or, enter q to quit: ") # might need spacing
    calc2 = raw_input() 
    if calc2 == "q": # needs fix
        break
    calc2 = float(calc2) 
    print("enter an operation to perform on the two operators (+ or -): ") 
    operation = raw_input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2)) # needs fix
    elif operation == '-': # wrong
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2)) # needs fix
    else:
        print("\n Not a valid entry. Restarting...")
