def greatest_common_divisor(a, b):
    if b == 0:
        return abs(a)
    return greatest_common_divisor(b, a % b)