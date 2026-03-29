#4. Convert string to uppercase without using built-in functions

s = input("Enter a string: ")
upper_s = ""

for char in s:
    if 'a' <= char <= 'z':
        upper_s += chr(ord(char) - 32)
    else:
        upper_s += char 

print("Uppercase string:", upper_s)
