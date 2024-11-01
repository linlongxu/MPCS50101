def centered_average_with_iteration(numbers):
    """Approach 1 - Using iteration"""
    if len(numbers) < 3:
        raise ValueError("List must contain at least three numbers.")
    
    # Find the unique minimum and maximum values
    min_val = min(numbers)
    max_val = max(numbers)

    filtered_numbers = []
    min_found = False
    max_found = False
    
    for num in numbers:
        if num == min_val and not min_found:
            min_found = True  # Skip the first instance of the minimum
        elif num == max_val and not max_found:
            max_found = True  # Skip the first instance of the maximum
        else:
            filtered_numbers.append(num)

    # Calculate the centered average
    average = sum(filtered_numbers) / len(filtered_numbers)
    return average


def centered_average(numbers):
    """Approach 2 - No iteration allowed"""
    if len(numbers) < 3:
        raise ValueError("List must contain at least three numbers.")
    
    # Using set to find unique values and sorting
    unique_numbers = list(set(numbers))
    
    # If there are only two unique numbers, return the average of those
    if len(unique_numbers) == 2:
        return sum(unique_numbers) / 2
    
    unique_numbers.sort()
    
    # Remove the first and last element (smallest and largest)
    centered_values = unique_numbers[1:-1]
    
    # Calculate the centered average
    if len(centered_values) == 0:
        raise ValueError("Not enough unique values to calculate a centered average.")
    
    average = sum(centered_values) / len(centered_values)
    return average


# Example Test Cases
numbers = [1, 4, 5, 6, 100]
print(f"Centered average (iteration): {centered_average_with_iteration(numbers)}")
print(f"Centered average (no iteration): {centered_average(numbers)}")

# Testing with an edge case
numbers_edge_case = [5, 5, 5, 5, 100]
print(f"Centered average (iteration): {centered_average_with_iteration(numbers_edge_case)}")
print(f"Centered average (no iteration): {centered_average(numbers_edge_case)}")