#include <bits/stdc++.h>
using namespace std;
 
struct Point {
    int x, y;
};
 
// Returns Total Area  of two overlap
// rectangles
int overlappingArea(Point l1, Point r1, 
                    Point l2, Point r2)
{
    // Area of 1st Rectangle
    int area1 = abs(l1.x - r1.x) 
      * abs(l1.y - r1.y);
 
    // Area of 2nd Rectangle
    int area2 = abs(l2.x - r2.x) 
      * abs(l2.y - r2.y);
 
    int x_dist = min(r1.x, r2.x) 
                  - max(l1.x, l2.x);
    int y_dist = (min(r1.y, r2.y) 
                  - max(l1.y, l2.y));
    int areaI = 0;
    if( x_dist > 0 && y_dist > 0 )
    {
        areaI = x_dist * y_dist;
    }
     
    return (areaI); // se >= 0, tem pontos em comum
}
 

int main(){



}