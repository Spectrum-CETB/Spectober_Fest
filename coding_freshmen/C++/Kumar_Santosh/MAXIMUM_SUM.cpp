#include<bits/stdc++.h>

using namespace std;

//template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
//template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
//void dbg_out() { cerr << endl; }
//template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
//#ifdef LOCAL
//#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
//#else
//#define dbg(...)
//#endif

#define ll long long
//#define ld long double
//#define ull unsigned long long
//#define vec vector
//#define uset unordered_set
//#define umap unordered_map
//#define mset multiset
//#define pub push_back
//#define pof pop_front
//#define pob pop_back
//#define puf push_front
//#define ff first
//#define ss second
//#define M 1000000007
#define IMX INT_MAX
#define IMN INT_MIN
#define yes cout<<"YES"<<endl
#define no cout<<"NO"<<endl
#define foarr(a, n) for(int i = 0; i<n; i++) cin>>a[i];
#define fo(n) for(int i = 0; i<n; i++) 

const int MAX_N = 1e5 + 5;
int sum=0;

void answer() {
    ll n;
    cin>>n;
    int arr[n];
    foarr(arr,n);
    int MAXsum=IMN;
    fo(n){
        sum+=arr[i];
        MAXsum=max(MAXsum,sum);
        if(sum<0) sum=0;
    }
    cout<<MAXsum<<endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tct;
    cin >> tct;
    for (int u = 1; u <= tct; u++) {
        // cout << "Case #" << t << ": ";
        answer();
    }
}
