# Check if a number is Armstrong.

def armstrong_number(number, p):
    res = 0
    while number!=0:
        rem = number%10
        res+= (rem**p)
        number//=10

    return res


number = int(input("Enter a number : "))
p = len(str(number))+1
arm_number = armstrong_number(number, p)
if arm_number == number:
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is not an armstrong number.")