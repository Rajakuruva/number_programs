# Check if a number is perfect

def fact_number(n):
    if n == 1 or n ==2:
        return n
    fact = 1
    for a in range(1, n+1):
        fact*=a
    return fact

def perfect_number(number):
    res = 0
    while number!=0:
        rem = number%10
        res+= fact_number(rem)
        number//=10

    return res

number = int(input("Enter a number : "))
result = perfect_number(number)
if result==number:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")