#4. Find the sum of digits of a number

num = int(input("Enter number: "))
sum_digits = 0
temp = num

while temp > 0:
    digit = temp % 10   
    sum_digits += digit    
    temp = temp // 10     

print("Sum of digits:", sum_digits)
