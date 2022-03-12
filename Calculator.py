menuList = ["", 'Welcome to Basic Calculator', '******************************************',
            'Enter + for addition', 'Enter - for subtraction', 'Enter * for multiplication',
            'Enter / for division', 'Enter e to exit','******************************************'
            ]

def addition_1(a, b):
    result1 = float(a) + float(b)
    return result1

def subtract_1(a,b):
    result1 = float(a) - float(b)
    return result1

def multiply_1(a,b):
    result1 = float(a) * float(b)
    return result1

def division_1(a,b):
    result1 = float(a) / float(b)
    return result1


def input_x():
    while True:
        try:
            a = input("please input the first number: ")
            if a == "c":
                quit("Thank you for using the calculator")
            elif int(a) == int(a):
                return a
        except ValueError:
            print("Please enter a number")


def input_y():
    while True:
        try:
            a = input("Please input the second number: ")
            if a == "c":
                quit("Thank you for using the calculator")
            elif int(a) == int(a):
                return a
        except ValueError:
            print("Please enter a number")

def input_y_division():
    while True:
        try:
            a = input("Please input the second number: ")
            if a == "c":
                quit("THANK YOU")
            if a == "0" or a == 0:
                print("Can't divide by 0, please enter a number except 0(zero)")
            elif int(a) == int(a):
                return a
        except ValueError:
            print("Please enter a number")


##### PROGRAM STARTS HERE#############

for i in menuList:
    print(i)
answers = []
while True:
    operation = input("Enter here an operator: ")
    if operation == "+":
        print("Enter C if you want to exit")
        x = input_x()
        y = input_y()
        z = addition_1(x, y)
        print(f"Answer is: {z}")
        print("Your list of answer")
        answers.append(z)
        print(f"Answer List: {answers}")

    elif operation == "-":
        print("Enter C if you want to exit")
        x = input_x()
        y = input_y()
        z = subtract_1(x, y)
        print(f"Answer is: {z}")
        answers.append(z)
        print(f"Answer List: {answers}")

    elif operation == "*":
        print("Enter C if you want to exit")
        x = input_x()
        y = input_y()
        z = multiply_1(x, y)
        print(f"Answer is: {z}")
        answers.append(z)
        print(f"Answer List: {answers}")

    elif operation == "/":
        x = input_x()
        y = input_y_division()
        z = division_1(x, y)
        print(f"Answer is: {z}")
        answers.append(z)
        print(f"Answer List: {answers}")

    elif operation == "e":
        quit()

    else:
        print("Invalid key")
