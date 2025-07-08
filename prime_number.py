# Given number is prime or not
def check_prime_number(number):
    if number<=1:
        return False
    
    for a in range(1, number//2+1):
        if number%a==0:
            return False
    return True

n = int(input("Enter a number : "))
if check_prime_number(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is not a prime number")
    