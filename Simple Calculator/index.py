# Take the input by the user
num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

# Take the Operator by the user
operator = input("Choose the operator : (+, -, *, / :)")

# Perform the Operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Choose Wrong Operator"
print("The Result is :" , result)
