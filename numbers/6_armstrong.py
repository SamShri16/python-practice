#6. Check whether a number is an Armstrong number

num = int(input("Enter number: "))
temp = num
sum_digits = 0
n = len(str(num))  # number of digits

while temp > 0:
    digit = temp % 10
    sum_digits += digit ** n
    temp = temp // 10

if sum_digits == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
