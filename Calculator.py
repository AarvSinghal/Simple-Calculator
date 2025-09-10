def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("==== Simple Calculator ====")
    print("Available operations: +, -, *, /")

    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == "+":
                result = add(a, b)
            elif operation == "-":
                result = subtract(a, b)
            elif operation == "*":
                result = multiply(a, b)
            elif operation == "/":
                result = divide(a, b)
            else:
                result = "Invalid operation!"

            print("Result:", result)
            try:
               again = input("Do you want to calculate again? (yes/no): ").lower()
               if again=="yes":
                   break
               elif again != "yes" and again=="no":
                   print("Exiting calculator. Goodbye!")
                   break
               else:
                   print("Invalid input! Try again")
                   raise Exception("Invalid output")
            except Exception as Invalidoutput:
                print("Try again")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    calculator()
