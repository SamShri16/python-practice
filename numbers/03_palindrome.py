#3. Check whether a number is a palindrome

num = int(input("Enter number: "))

temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed no. is: ", rev)    

if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")
