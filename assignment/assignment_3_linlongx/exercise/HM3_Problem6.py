import math

def read_points(filename):
    """Read points from a text file and return a list of tuples."""
    points = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            point_name = parts[0]
            coordinates = tuple(float(part) for part in parts[1:])
            points.append((point_name, coordinates))
    return points

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points in 3D space."""
    return math.sqrt((point1[0] - point2[0]) ** 2 +
                     (point1[1] - point2[1]) ** 2 +
                     (point1[2] - point2[2]) ** 2)

def closest_point_to_origin(points):
    """Find the closest point to the origin."""
    origin = (0.0, 0.0, 0.0)
    closest_point = None
    min_distance = float('inf')
    
    for point_name, coordinates in points:
        distance = euclidean_distance(origin, coordinates)
        if distance < min_distance:
            min_distance = distance
            closest_point = (point_name, coordinates)
    
    return closest_point, min_distance

def closest_points(points):
    """Find the two closest points to each other."""
    min_distance = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i][1], points[j][1])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    
    return closest_pair, min_distance

# Read points from the file
points = read_points("/Users/simpson/Desktop/MPCS/assignment/assignment_3_linlongx/exercise/points.txt")

# Find the closest point to the origin
closest_to_origin, distance_to_origin = closest_point_to_origin(points)
print(f"Closest point to the origin: {closest_to_origin[0]} at coordinates {closest_to_origin[1]} with distance {distance_to_origin:.2f}")

# Find the closest points to each other
closest_pair, distance_between_closest = closest_points(points)
print(f"Closest points are: {closest_pair[0][0]} at {closest_pair[0][1]} and {closest_pair[1][0]} at {closest_pair[1][1]} with distance {distance_between_closest:.2f}")