# implementation from https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/ adding constraining clause

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
def on_line(p, q, r):
    return min(p.x, r.x) <= q.x <= max(p.x, r.x) and min(p.y, r.y) <= q.y <= max(p.y, r.y) and \
           (r.x - p.x) * (q.y - p.y) == (q.x - p.x) * (r.y - p.y)

# Checking if a point is inside a polygon
def point_in_polygon(point, polygon):
    num_vertices = len(polygon)
    x, y = point.x, point.y
    inside = False
 
    # Store the first point in the polygon and initialize the second point
    p1 = polygon[0]
    

    # Loop through each edge in the polygon
    for i in range(1, num_vertices + 1):
        # Get the next point in the polygon
        p2 = polygon[i % num_vertices]

        if on_line(p1, point, p2): return True
 
        # Check if the point is above the minimum y coordinate of the edge
        if y > min(p1.y, p2.y):
            # Check if the point is below the maximum y coordinate of the edge
            if y <= max(p1.y, p2.y):
                # Check if the point is to the left of the maximum x coordinate of the edge
                if x <= max(p1.x, p2.x):
                    # Calculate the x-intersection of the line connecting the point to the edge
                    x_intersection = (y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x
 
                    # Check if the point is on the same line as the edge or to the left of the x-intersection
                    if p1.x == p2.x or x <= x_intersection:
                        # Flip the inside flag
                        inside = not inside
 
        # Store the current point as the first point for the next iteration
        p1 = p2
 
    # Return the value of the inside flag
    return inside
 
# Driver code
if __name__ == "__main__":
    n, q = [int(x) for x in input().split()]

    polygon = []
    inp = [int(x) for x in input().split()]

    for i in range(n):
        curr = []
        a = inp[2*i]
        b = inp[2*i + 1]
        polygon.append(Point(a, b))
    
    for _ in range(q):
        a, b = [int(x) for x in input().split()]
        if point_in_polygon(Point(a, b), polygon):
            print("D")
        else:
            print("F")
