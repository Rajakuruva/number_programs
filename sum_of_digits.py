#  Find the sum of digits of a number
def sum_of_digits(number):
    sum = 0
    while number!=0:
        rem = number%10
        sum+=rem
        number//=10
    return sum

number = int(input("Enter a number : "))
sum_num = sum_of_digits(number)
print(f"Sum of {number} is {sum_num}")