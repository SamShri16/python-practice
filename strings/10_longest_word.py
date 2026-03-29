#10. Find the longest word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
