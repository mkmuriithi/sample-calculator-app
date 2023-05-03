class Calculator:

    def add(self,x,y):
        return x + y

    def subtract(self,x,y):
        return x - y

    def divide(self,x,y):
        return x / y

    def mulitply(self,x,y):
        return x * y


if __name__ == "__main__":
    
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))

    operation = int(input("Enter operation: 1:add, 2: subtract, 3:divide, 4:multiple -> "))


    myCalculator = Calculator()
    result = 0
    if(operation == 1):
        result = myCalculator.add(a,b)
    elif(operation == 2):
        result = myCalculator.subtract(a,b)
    elif(operation == 3):
        result = myCalculator.multiply(a,b)
    elif(operation == 4):
        result = myCalculator.divide(a,b)
    else:
        print("Please enter a valid value for the operation")

    print("Result: " + str(result) + "\n")
