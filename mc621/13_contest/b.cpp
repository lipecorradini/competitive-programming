#include <bits/stdc++.h>
using namespace std;

// overlapping area from two rectangles from https://www.geeksforgeeks.org/total-area-two-overlapping-rectangles/
// overlapping existance from https://www.geeksforgeeks.org/find-two-rectangles-overlap/

struct Point {
    int x, y;
};

bool doOverlap(Point l1, Point r1, Point l2, Point r2)
{
   if (l1.x > r2.x || l2.x > r1.x)
        return false;

    // If one rectangle is above the other
    if (r1.y > l2.y || r2.y > l1.y)
        return false;

    return true;
}
 
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
     
    return (area1 + area2 - areaI);
}


int main() {
   ios::sync_with_stdio(false);
   cin.tie(0);

   vector<pair<Point, Point>> P;

    int t; cin >> t;

    while(t--){

        int n; cin >> n;

        vector<set<int>> mains;
        mains[0].emplace(0);

        // getting main value
        pair<Point, Point> main;
        cin >> main.first.x >> main.first.y >> main.second.x >> main.second.y;
        P.push_back(main);

        while(n--){
            
            pair<Point, Point> current;
            cin >> current.first.x >> current.first.y >> current.second.x >> current.second.y;
            
            // guardar retangulos numa lista
            P.push_back(current);

            bool isInMain = false;
            // para cada novo retangulo, ve aqueles com quem tem overlap
            for (int i = 0; i < P.size(); i++){
                pair<Point, Point> ret = P[i];
                if(doOverlap(current.first, current.second, ret.first, ret.second) && mains.find(i) != mains.end()){
                    // ou seja, o retangulo estara com os mains
                }
            }


        }
    }


    // para cada novo retangulo, ve aqueles com quem tem overlap
    //  mapear num set os indices dos retangulos que tem intersecao com o main
    // se o do overlap estiver no set, calcula a area e adiciona. 
    // depois, se tiver sido adicionado a area:
    //      itera de novo pelos retangulos do overlap, e adiciona a area de todos
    // printa a area final




}
