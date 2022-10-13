#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s,t;
    cin >> s >> t;
    if(s.length()!=t.length()){
        cout << "false" << endl;
        exit(0);
    }
    int fr[26] = {0};
    string ans = "true";
    for(auto i:s){
        fr[i - 'a']++;
    }
    for(auto i:t){
        if(fr[i-'a']==0){
            ans = "false";
            break;
        }else{
            fr[i - 'a']--;
        }
    }
    cout << ans << endl;
    return 0;
}