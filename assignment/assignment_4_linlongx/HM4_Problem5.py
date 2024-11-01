import math
from HM4_Problem4 import generate

def calculate_statistics(data):
    n = len(data)
    mean = sum(data) / n
    median = sorted(data)[n // 2] if n % 2 == 1 else (sorted(data)[n // 2 - 1] + sorted(data)[n // 2]) / 2
    mode = max(set(data), key=data.count)
    variance = sum((x - mean) ** 2 for x in data) / n
    stddev = math.sqrt(variance)
    
    return mean, median, mode, variance, stddev

# Main
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
        data = generate(count, True)
    else:
        data = generate(100, True)
    
    mean, median, mode, variance, stddev = calculate_statistics(data)
    print(f"mean: {mean}\nmedian: {median}\nmode: {mode}\nvariance: {variance}\nstandard deviation: {stddev}")
