import random

def generate(numbers_to_generate, write_to_file):
    numbers = [random.randint(0, 100) for _ in range(numbers_to_generate)]
    sorted_numbers = sorted(numbers)
    
    if write_to_file:
        with open("numbers.txt", "w") as file:
            file.write("\n".join(map(str, sorted_numbers)))
    
    return sorted_numbers