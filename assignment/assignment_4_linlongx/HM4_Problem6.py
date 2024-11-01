import statistics

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

# Main
data = read_numbers_from_file("numbers.txt")
print(f"mean: {statistics.mean(data)}")
print(f"median: {statistics.median(data)}")
print(f"mode: {statistics.mode(data)}")
print(f"variance: {statistics.variance(data)}")
print(f"standard deviation: {statistics.stdev(data)}")