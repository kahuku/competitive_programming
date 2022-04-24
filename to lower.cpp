#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    int p, t;
    cin >> p >> t;
    int solved = 0;
    for (int i = 0; i < p; i++){
        int passed = 0;
        for (int j = 0; j < t; j++){
            string test;
            cin >> test;
            vector<char> v(test.begin(), test.end());
            v[0] = tolower(v[0]);
            bool lower = true;
            for (int k = 0; k < v.size(); k++){
                if (!islower(v[k])){
                    lower = false;
                }
            }
            if (lower){
                passed++;
            }
        }
        if (passed == t){
            solved++;
        }
    }
    cout << solved;
    return 0;
}
