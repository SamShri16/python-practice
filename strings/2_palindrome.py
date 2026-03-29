#2. Check whether a string is a palindrome

s = input("Enter a string: ")

reversed_s = s[::-1]

if s == reversed_s:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
