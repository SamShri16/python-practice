#3. Reverse an array

arr = input("Enter array elements separated by space: ").split()
arr = [int(x) for x in arr]

n = len(arr)

for i in range(n // 2):
    
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print("Reversed array:", arr)
