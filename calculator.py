# Create a basic calculator that can perform basic arithemetic operation such as addition, subtraction, multiplication, and division functions


# This function add two numbers
def add(x, y):
    """Function to model the addition operation"""
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    """Function to model the subtraction operation"""
    return x - y

#This function multiply two numbers
def multiply(x, y):
    """Function to model multilication operation"""
    return x * y

# This function divide two numbers
def divide(x, y):
    """Function to model division operation"""
    return x / y


# A list of the available operators for this calculator
print("Select operation ::::\n")
operators = ["+", "-", "/", "*"]

# print out the operators horizontally seperated with a line |
for index, operator in enumerate(operators):
    #check to avoid print | at the last element
    if index == len(operators) - 1:
        print(operator)
    else:
        print(operator, end=" | ")

while True:
    choice = input("\nEnter an operator to work with ::::: ")
    if choice in operators:
        num_1 = float(input("Enter the first value ::: "))
        num_2 = float(input("Enter the second value ::: "))

        # perform addition operation
        if choice == "+":
            add_num = add(num_1, num_2)
            print(num_1,"+", num_2, "=" ,add_num)
            break

        #perform subtraction operation
        elif choice == "-":
            subtract_num = subtract(num_1, num_2)
            print(num_1,"-", num_2, "=" ,subtract_num)
            break

        #perform dvision operation
        elif choice == "/":
            divide_num = divide(num_1, num_2)
            print(num_1,"/", num_2, "=" ,divide_num)
            break
        
        #perform multiplication operation
        elif choice == "*":
            multiply_num = multiply(num_1, num_2)
            print(num_1,"*", num_2, "=" ,multiply_num)
            break

        #Test case if none of the valid operators are inputted
    else:
        print("Please enter a valid operator from the list above!!!")