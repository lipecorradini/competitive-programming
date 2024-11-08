#include <bits/stdc++.h>
using namespace std;

// overlapping area from two rectangles from https://www.geeksforgeeks.org/total-area-two-overlapping-rectangles/
// overlapping existance from https://www.geeksforgeeks.org/find-two-rectangles-overlap/

struct Point {
    int x, y;
};

bool doOverlap(Point l1, Point r1, Point l2, Point r2)
{
   if (r1.x <= l2.x)
        return false;

    // If one rectangle is above the other
    if (r1.y <= l2.y || r2.y <= l1.y)
        return false;

    return true;
}
 

int main(){
    int t; cin >> t;
    while (t--){
        
        pair<Point, Point> ret1;
        pair<Point, Point> ret2;

        cin >> ret1.first.x >> ret1.first.y >> ret1.second.x >> ret1.second.y;
        cin >> ret2.first.x >> ret2.first.y >> ret2.second.x >> ret2.second.y;

        vector<pair<Point, Point>> vec;
        
        if(ret1.first.x <= ret2.first.x){
            vec.push_back(ret1);
            vec.push_back(ret2);
        }else{
            vec.push_back(ret2);
            vec.push_back(ret1);
        }
        // cout << "aaaaaaa\n";

        ret1 = vec[0];
        ret2 = vec[1];

        Point l1 = ret1.first;
        Point r1 = ret1.second;
        Point l2 = ret2.first;
        Point r2 = ret2.second;


        if (!doOverlap(ret1.first, ret1.second, ret2.first, ret2.second)){
            cout << "No Overlap" << endl;
        }else{
            cout << max(l1.x, l2.x) << " " << max(l1.y, l2.y) << " " << min(r1.x, r2.x) << " " << min(r1.y, r2.y) << endl;
        }

        if(t) cout << endl;


    }
}