#8. Find GCD and LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find GCD
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x

# Find LCM
lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
