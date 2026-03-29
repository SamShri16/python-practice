#7. Move all zeros to end of array

arr = input("Enter array elements separated by space: ").split()
arr = [int(x) for x in arr]

result = []

for num in arr:
    if num != 0:
        result.append(num)

zero_count = len(arr) - len(result)

for i in range(zero_count):
    result.append(0)

print("Array after moving zeros:", result)
