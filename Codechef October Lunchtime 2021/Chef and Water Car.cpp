#include<bits/stdc++.h>
#define int long long
#define vi vector<int>
#define  pb push_back
#define inf INT_MAX
#define minf INT_MIN
#define mod 1000000007
#define bits1 __builtin_popcountl
#define  fio ios_base::sync_with_stdio(NULL) ; cin.tie(NULL) ;
using namespace std ;
signed main()
{
int t;
 cin>>t;
 while(t--)
 {
    int n,v ;
    cin>>n>>v ;
    int ans=n*(n-1)/2 ;
    cout<<ans ;
    cout<<" " ;
    if(v>=n-1)
    {
        cout<<n-1<<"\n" ;
    }
    else
    {
        int res=n-v ;
        ans=res*(res+1)/2 ;
        ans=ans+(v-1) ;
        cout<<ans<<"\n" ;
    }
 }
return 0 ;
}