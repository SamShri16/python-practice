#2. Calculate the sum of elements in an array

arr = input("Enter array elements separated by space: ").split()
arr = [int(x) for x in arr] 

sum_elements = 0 

for num in arr:
    sum_elements += num 

print("Sum of elements:", sum_elements)
