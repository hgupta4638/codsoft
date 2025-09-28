print("---Welcome to simple calculator app---")

num1 = float(input("Enter first number: "))

print("Select operation which you want:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice(1-4): ")

num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
    operator = '+'
elif choice == '2':
    result = num1 - num2
    operator = '-'
elif choice == '3':
    result = num1 * num2
    operator = '*'
elif choice == '4':
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
    operator = '/'
else:
    result = "Invalid choice!"
    operator = ''

if operator != '':
    print(f"{num1} {operator} {num2} = {result}")
else:
    print(result)