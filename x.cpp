#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#else
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <queue>
#include <functional>
#include <stack>
#include <map>
#include <cstring>
#include <set>
#include <unordered_map>
#include <unordered_set>
#endif

#define fastio() cin.tie(0);ios::sync_with_stdio(0);
#define pii pair<int, int>
#define fi first
#define se second
#define mp make_pair
#define el "\n"
#define pq priority_queue
#define ll long long
#define ld long double
#define ull unsigned long long
#define mt make_tuple
#define vi vector<int>
#define pb push_back
#define eb emplace_back
#define dq deque
#define uset unordered_set
#define umap unordered_map

using namespace std;

const int NINF = -0x3f3f3f3f;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;



int main() {
    int n, m, c;
    c=0;
    cin >> n >> m;
    int ns[n];
    int ms[m]; q
    for (int i = 0; i < n; i++) {
        int a; cin >> a;
        ns[i] = a-i;
        deadn[i] = ns[i]==-1;
    }
    for (int i = 0; i < m; i++) {
        cin >> ms[i];
        deadm[i] = ns[i]==-1;
        if (deadm[i]) continue;
        for (int j = 0; j < n; j++) {
            if (deadn[j]) continue;
            if (ns[j]+i == ms[i]+j) {
                deadn[j] = true;
                deadm[i] = true;
                c++;
                break;
            }
        }
    }
    cout << c << endl;
}