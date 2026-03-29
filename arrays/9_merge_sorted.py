#9. Merge two sorted arrays

arr1 = input("Enter first sorted array: ").split()
arr2 = input("Enter second sorted array: ").split()

arr1 = [int(x) for x in arr1]
arr2 = [int(x) for x in arr2]

i = 0
j = 0
merged = []

# Merge both arrays
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

# Add remaining elements
while i < len(arr1):
    merged.append(arr1[i])
    i += 1

while j < len(arr2):
    merged.append(arr2[j])
    j += 1

print("Merged array:", merged)
