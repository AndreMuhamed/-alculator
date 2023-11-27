# Function for addition
def addition(x, y):
    return x + y

# Function for subtraction
def subtraction(x, y):
    return x - y

# Function for multiplication
def multiplication(x, y):
    return x * y

# Function for division
def division(x, y):
    if y == 0:
        return "Division by zero is not possible"
    else:
        return x / y

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Choosing operation
choice = input("Enter operation number (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", addition(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtraction(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiplication(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("Invalid operation chosen")
