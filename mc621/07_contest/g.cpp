#include <bits/stdc++.h>

using namespace std;

// codigo amplamente baseado nos slides da disciplina 

typedef vector<int> vi;
vi primes; 

long long EulerPhi(long long N) {
    
    long long ans = N;
    long long PF_idx = 0, PF = primes[PF_idx];
    ans = N;
    
    while (N != 1 && (PF * PF <= N)) {
        if (N % PF == 0) ans -= ans / PF; 
        while (N % PF == 0) N /= PF;
        PF = primes[++PF_idx];
    }
    
    if (N != 1) ans -= ans / N; 
    return ans;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);


    int t; cin >> t;
    while(t -- ){
        int a; cin >> a;
        cout << EulerPhi(a) << endl;
    }

}
