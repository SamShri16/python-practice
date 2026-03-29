#10. Check whether a number is a perfect number

num = int(input("Enter number: "))
sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
