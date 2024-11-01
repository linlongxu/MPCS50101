def process_file(filename):
    """Read, sort and return a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Read lines
            lines = [line.strip() for line in file.readlines()]
        
        # Remove empty lines
        lines = [line for line in lines if line]
        # Sort the contents
        sorted_items = sorted(lines)
        # Number of lines
        number_of_lines = len(sorted_items)
        # Return a tuple
        return filename, sorted_items, number_of_lines

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return filename, [], 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return filename, [], 0

# Snippet to run function
filename, items, lines = process_file("/Users/simpson/Desktop/MPCS/assignment/assignment_3_linlongx/exercise/common_words.txt")

# Print the contents of the tuple
print(f"Filename: {filename}")
print(f"Sorted Items: {items}")
print(f"Number of Lines: {lines}")
