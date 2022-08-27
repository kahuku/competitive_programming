#include <iostream>
#include <string>
#include <set>
using namespace std;
int main() {
    string line;
    int num;
    set<int> s;
    for (int i = 0; i < 10; i++){
        cin >> num;
        s.insert(num % 42);
    }
    cout << s.size() << endl;
    return 0;
}
