#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    string S;
    cin >> S;
    int n = S.length();
    int last[26];
    for(int i=0;i<26;i++) last[i] = -1; //inicializo com -1
    
    ll total = 0;
    int start = 0;
    
    for(int end = 0; end < n; end++){
        int charIdx = S[end] - 'a';
        if(last[charIdx] >= start){
            start = last[charIdx] + 1; // comeca no proximo caractere
        }
        last[charIdx] = end; // atualiza ultima aparixcao
        total += (end - start + 1); //adicioa numero novo de substrings
    }
    
    cout << total << endl;
}
