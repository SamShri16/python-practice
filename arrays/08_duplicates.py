#8. Find duplicate elements in array

arr = input("Enter array elements separated by space: ").split()
arr = [int(x) for x in arr]

duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate elements:", duplicates)
