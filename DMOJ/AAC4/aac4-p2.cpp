#include <iostream>
#include <math.h>
#include <algorithm>


using namespace std;

const int MAXN = 2e5 + 3;

int n, q, plcm[MAXN];

int bs(int num) {
    int l = 1, r = n;
    
    while (l < r) {
        int mid = (l + r) / 2;
        if (num % plcm[mid] == 0) l = mid + 1;
        else r = mid;
    }

    l += (num % plcm[l] == 0);
    if (l > n) return -1;
    return l;
}

int main() {
    cin >> n >> q;

    for (int i = 1; i <= n; i++) {
        int a; cin >> a;
        if (i == 1) plcm[i] = a;
        else {
            if (plcm[i - 1] >= 1e9) pcm[i] = 1e9 + 1;
            else pcm[i] = lcm(plcm[i - 1], a);
        }
    }

    while (q--) {
        int num; cin >> num;

        cout << bs(num) << '\n';
    }
}
