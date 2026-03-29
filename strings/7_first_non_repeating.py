#7. Find the first non-repeating character

s = input("Enter a string: ")

for char in s:
    if s.count(char) == 1:  
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found")
