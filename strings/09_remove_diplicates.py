#9. Remove duplicate characters from a string

s = input("Enter a string: ")
result = ""

for char in s:
    if char not in result:
        result += char

print("String without duplicates:", result)
