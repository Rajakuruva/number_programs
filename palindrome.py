# Check if a number is a palindrome.
def palindrome_number(number):
    res = 0
    while number!=0:
        rem = number%10
        res = (res*10) + rem
        number//=10
    return res

number = int(input("Enter a number : "))
result = palindrome_number(number)
if number == result:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")