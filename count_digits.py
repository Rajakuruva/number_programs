#  Count the number of digits in a number
def count_number(number):
    str_num = str(number)
    count_digits = len(str_num)
    return count_digits

number = int(input("Enter a number : "))
count_result = count_number(number)
print(f"Count the number of digits in the {number} is {count_result}")

#  Alternative (without converting to string):
def count_digits(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

n = int(input("Enter a number : "))
number_count = count_number(number)
print(f"Count the number of digits in the {n} is {number_count}")
