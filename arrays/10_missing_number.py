#10. Find missing number in an array (1 to n)

arr = input("Enter array elements: ").split()
arr = [int(x) for x in arr]

n = len(arr) + 1

for num in range(1, n + 1):
    if num not in arr:
        print("Missing number:", num)
        break
