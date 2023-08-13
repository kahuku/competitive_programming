// emergent trading summer 2023 internship interview
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a_size;
    int prev;
    int curr;
    
    cin >> a_size;
    cin >> prev;
    
    for (int i = 0; i < a_size - 1; i++) {
        cin >> curr;
        if (curr < prev) {
            cout << i << endl;
            return 0;
        }
    }
    cout << 0 << endl;
    return 0;
}