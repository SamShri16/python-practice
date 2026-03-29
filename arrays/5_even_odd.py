#5. Count even and odd numbers in an array

arr = input("Enter array elements separated by space: ").split()
arr = [int(x) for x in arr]

even_count = 0
odd_count = 0

for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
