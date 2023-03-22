from art import logo
print(logo)

end_of_calculation = False

def calculator(f_number, operation, second_number):
    if operation == "+":
        return f_number + second_number
    elif operation == "-":
        return f_number - second_number
    elif operation == "*":
        return f_number * second_number
    elif operation == "/":
        return f_number / second_number
    

while end_of_calculation != True:
    first_number = float(input("What's the first number?:"))
    choice_of_operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))
    output = calculator(first_number, choice_of_operation, next_number)
    print(f"{first_number} {choice_of_operation} {next_number} = {output}")
    continue_calculating = input(f"Type 'y' to continue or type 'n' to start a new calculation")
    if continue_calculating == "y":
        first_number = output
    elif continue_calculating == "n":
        end_of_calculation = True