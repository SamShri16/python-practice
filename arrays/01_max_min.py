#1. Find the maximum and minimum element in an array

arr = input("Enter array elements separated by space: ").split()
arr = [int(x) for x in arr]  

max_element = arr[0]
min_element = arr[0]

for num in arr:
    if num > max_element:
        max_element = num
    if num < min_element:
        min_element = num

print("Maximum element:", max_element)
print("Minimum element:", min_element)
