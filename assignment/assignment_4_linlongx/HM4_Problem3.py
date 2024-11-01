def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

# Main
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", greatest_common_divisor(a, b))