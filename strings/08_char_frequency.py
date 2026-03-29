#8. Count frequency of each character

s = input("Enter a string: ")

freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character frequencies:")
for char, count in freq.items():
    print(char, ":", count)
