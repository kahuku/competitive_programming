// #include <bits/stdc++.h> // need to do some more work to get this mega-include working
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int r, c;

typedef vector<char> vc;
typedef vector<vc> vvc;

typedef vector<bool> vb;
typedef vector<vb> vvb;

vvc grid;
vvb danger;

int gold = 0;

void solve(int i, int j) {
    if (grid[i][j] == 'G') ++gold;
    if (grid[i][j] == '#') return;

    grid[i][j] = '#';

    if (danger[i][j]) return;

    solve(i, j-1);
    solve(i, j+1);
    solve(i-1, j);
    solve(i+1, j);
}

int main() {
    cin >> c >> r;
    grid.assign(r, vc(c));
    danger.assign(r, vb(c, false));

    for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) cin >> grid[i][j];

    // for (auto row : grid) {
    //     for (auto i : row) cout << i;
    //     cout << endl;
    // }

    int si, sj;
    for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) {
        if (grid[i][j] == 'P') si = i, sj = j;
        else if (grid[i][j] == 'T') {
            danger[i][j - 1] = true;
            danger[i][j + 1] = true;
            danger[i - 1][j] = true;
            danger[i + 1][j] = true;
        }
    }

    solve(si, sj);
    cout << gold << endl;
    return 0;
}