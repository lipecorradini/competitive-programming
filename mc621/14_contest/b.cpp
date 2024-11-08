
// C++ program for the above approach
#include <bits/stdc++.h>
 
// algorithm extracted from https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/

using namespace std;
 
struct Point {
    int x, y;
};
 
// Checking if a point is inside a polygon
bool point_in_polygon(Point point, vector<Point> polygon)
{
    int num_vertices = polygon.size();
    int x = point.x, y = point.y;
    bool inside = false;
 
    // Store the first point in the polygon and initialize
    // the second point
    Point p1 = polygon[0], p2;
    
    for (int i = 0; i <= num_vertices; i++){
        if(x == polygon[i].x && y == polygon[i].y){
            return true;
        }
    }
    
    // Loop through each edge in the polygon
    for (int i = 1; i <= num_vertices; i++) {
        // Get the next point in the polygon
        p2 = polygon[i % num_vertices];
 
        // Check if the point is above the minimum y
        // coordinate of the edge
        if (y > min(p1.y, p2.y)) {
            // Check if the point is below the maximum y
            // coordinate of the edge
            if (y <= max(p1.y, p2.y)) {
                // Check if the point is to the left of the
                // maximum x coordinate of the edge
                if (x <= max(p1.x, p2.x)) {
                    // Calculate the x-intersection of the
                    // line connecting the point to the edge
                    double x_intersection
                        = (y - p1.y) * (p2.x - p1.x)
                              / (p2.y - p1.y)
                          + p1.x;
 
                    // Check if the point is on the same
                    // line as the edge or to the left of
                    // the x-intersection
                    if (p1.x == p2.x
                        || x <= x_intersection) {
                        // Flip the inside flag
                        inside = !inside;
                    }
                }
            }
        }
 
        // Store the current point as the first point for
        // the next iteration
        p1 = p2;
    }
 
    // Return the value of the inside flag
    return inside;
}
 
// Driver code
int main()
{
    // Define a polygon
    vector<Point> polygon;

    int n, q;
    cin >> n >> q;

    Point a;
    for(int i = 0; i < n; i++){
        cin >> a.x >> a.y;
        polygon.push_back(a);
    }   
    
    for(int i = 0; i < q; i++){
        Point point;
        // Check if the point is inside the polygon
        cin >> point.x >> point.y;
        // point.x = c;
        // point.y = b;
        // cout << point.x << " " << point.y << endl;

        if (point_in_polygon(point, polygon)) {
            cout << "D" << endl;
        }
        else {
            cout << "F" << endl;
        }
    }
    
 
    return 0;
}
