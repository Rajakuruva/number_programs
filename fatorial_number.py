# Finding the factorial of the number
def factorial(number):
    fact = 1
    for a in range(1,number+1):
        fact*=a
    return fact

number = int(input("Enter a number : "))
factorial_number = factorial(number)
print(f"Factorial of {number} is {factorial_number}")