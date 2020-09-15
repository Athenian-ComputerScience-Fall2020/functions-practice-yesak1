'''
Adapt the code from one of the functions above to create a new function called 'multiplier'.
The user should be able to input two numbers that are stored in variables.
The function should multiply the two variables together and return the result to a variable in the main program.
The main program should output the variable containing the result returned from the function.
'''

def multiplier():
    # Stores two numbers in two variables.
    num1 = int(input("enter a number"))
    num2 = int(input("enter another number"))

# Adds the variable contents together and returns the total to the main program

    return num1 * num2

# Calls the adder function and stores the data returned
output_num = multiplier()

# Outputs the data in the outputNum variable
print(output_num)