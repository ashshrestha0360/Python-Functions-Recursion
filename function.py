def add(a, b):
    return (a + b)


def sub(a, b):
    return(a - b)


def prod(a, b):
    return(a * b)


def div(a, b):
    return(a / b)


while(True):
    n1 = float(input("Enter the first number \n"))
    n2 = float(input("Enter the second number \n"))
    print("1. Add\n 2. Subtract\n 3. Product\n 4. Divison\n 5. Exit")
    op = int(input("Enter the option"))
    if(op == 1):
        res = add(n1, n2)
        print("Result: ", res)
    elif(op == 2):
        res = sub(n1, n2)
        print("Result: ", res)

    elif(op == 3):
        res = prod(n1, n2)
        print("Result: ", res)

    elif(op == 4):
        res = div(n1, n2)
        print("Result: ", res)

    else:
        print("Wrong Input")
        break
print("Program Exited")
