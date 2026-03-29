#5. Find the length of string without using len()

s = input("Enter a string: ")
count = 0

for char in s:
    count += 1

print("Length of string:", count)
