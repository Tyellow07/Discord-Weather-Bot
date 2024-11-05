#include<bits/stdc++.h>
using namespace std;


signed main() {
  ios_base::sync_with_stdio(false), cin.tie(0);
  int n, m;
  cin >> n >> m;
  for(int v, u, i = 0; i < m; i++) {
    cin >> u > v;
    adj[u].pb(v);
    adj[v].pb(u);
  }
  int a, b;
  cin >> a >> b;
  cout << a + b << '\n';

}
