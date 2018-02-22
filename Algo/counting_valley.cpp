#include <bits/stdc++.h>

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
 
int main() {
    ll n;
    cin>>n;
    string s;
    cin>>s;
    ll upd=0,ans=0,prev=0;
    for(int i=0;i<s.size();i++){
        prev = upd;
        if(s[i] == 'D') --upd;
        else ++upd;
        if(upd == 0 && prev<0) ans++;
    }
    cout<<ans<<endl;
    return 0;
}