import math

def find_closest_point(points):
    closest_distance = float('inf')
    closest_point = (0, 0)

    for i in range(len(points[0])):
        x = points[0][i]
        y = points[1][i]

        if x >= 0 and y >= 0:
            distance = math.sqrt(x2 + y2)
            if distance < closest_distance:
                closest_distance = distance
                closest_point = (x, y)

    if closest_distance == float('inf'):
        return (0, 0)
    else:
        return closest_point