#6. Find all pairs with given sum (Two Sum problem)

arr = input("Enter array elements separated by space: ").split()
arr = [int(x) for x in arr]

target = int(input("Enter target sum: "))

n = len(arr)

print("Pairs with given sum:")

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])
