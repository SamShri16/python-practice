#3. Count vowels and consonants in a string

s = input("Enter a string: ").lower()  # convert to lowercase for simplicity

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in s:
    if char.isalpha():  # check if it's a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
