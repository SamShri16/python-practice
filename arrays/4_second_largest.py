#4. Find the second largest element in an array

arr = input("Enter array elements separated by space: ").split()
arr = [int(x) for x in arr]

largest = arr[0]
second_largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

second_largest = None

for num in arr:
    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num

print("Second largest element:", second_largest)
