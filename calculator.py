def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0 :
        return "can't divide by zero"
    return x / y
 
def calculator():
    while True:
        print("Select option:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Mutliplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting the calculator. GoodBye!")
            break
        
        if choice not in ('1','2','3','4'):
            print("Invalid Input")
            continue
        
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))    
        
        if choice == '1':
            print("Result: ", add(num1, num2))
        elif choice == '2':
            print("Result: ", subtract(num1, num2))
        elif choice == '3':
            print("Result: ", multiply(num1, num2))
        elif choice == '4':
            print("Result: ", divide(num1, num2))
   
calculator()