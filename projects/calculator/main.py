print("hello world")

def cal(a,b):

    print(".....choose operation.....")
    print("1: Addition")
    print("2: Subtraction")
    print("3: MUltiplication")
    print("4: Division")
    
    op = int(input("choose operation:"))

    if op==1:
        print(a+b)
    elif op==2:
        print(a-b)
    elif op==3:
        print(a*b)
    elif op==4:
        print(a/b)
    else:
        print("invalid operation")

a = int(input("enter number: "))
b = int(input("enter number: "))


cal(a,b)








def cal(a,b):


    op = input("choose operation:")

    if op=="+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op=="*":
        print(a*b)
    elif op=="/":
        print(a/b)
    elif b==0:
        print("zerodivision error")
    
    else:
        print("invalid operation")



stop = True
while stop:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    cal(a,b)
    print("1: continue")
    print("2: exit")
    num = int(input("choose to continue or exit."))
    if num == 2:
        stop = False








def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print(f"result: {num1+num2}")
        elif operator == "-":
            print(f"result: {num1-num2}")
        elif operator == "*":
            print(f"result: {num1*num2}")
        elif operator == "/":
            if num2==0:
                print('ZeroDivisionError')
            else:
                print(f"result: {num1/num2}")
        else:
            print("Invalid operator!")

        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice == "no":
            print("Calculator exited.")
            break


calculator()








def calculator():
    print("Type 'exit' to quit")
    while True:
        # Take the full expression as input
        expression = input("Enter expression (e.g., 5 + 3 * 2): ")

        # Exit condition
        if expression.lower() == "exit":
            print("Calculator exited.")
            break

        try:
            # Evaluate the expression safely
            result = eval(expression, {"__builtins__": None}, {})
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except Exception:
            print("Invalid expression!")

calculator()
















def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    
    while True:
        op = input("\nEnter operation (+, -, *, /) or 'q' to quit: ")
        if op.lower() == 'q':
            print("Exiting calculator... Bye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if op == '+':
            print("Result:", add(num1, num2))
        elif op == '-':
            print("Result:", subtract(num1, num2))
        elif op == '*':
            print("Result:", multiply(num1, num2))
        elif op == '/':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    calculator()
