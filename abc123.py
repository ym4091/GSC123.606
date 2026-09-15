def choose_operation():
    print("Which operation would you like to perform?")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    operation = int(input("Enter your choice: "))
    return operation


def enter_operand(operand_number):
    operand = int(input("Enter the " + operand_number + " number: "))
    return operand


def get_division_type():
    print("Which type of division?")
    print("1 - Regular division")
    print("2 - Integer division")

    division_type = int(input("Enter your choice: "))
    return division_type


def perform_operation(operation, operand1, operand2):
    result = 0

    if operation == 1:
        result = operand1 + operand2
    elif operation == 2:
        result = operand1 - operand2
    elif operation == 3:
        result = operand1 * operand2
    elif operation == 4:
        division_type = get_division_type()

        if division_type == 1:
            result = operand1 / operand2
        else:
            result = operand1 // operand2

    return result


def main():
    print("Welcome to the Python calculator!")

    operation = choose_operation()
    operand1 = enter_operand("first")
    operand2 = enter_operand("second")

    result = perform_operation(operation, operand1, operand2)
    print("Result:", result)


main()