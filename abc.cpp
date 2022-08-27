#include <iostream>
#include <queue>
#include <string>
using namespace std;
int main() {
    int x, y, z;
    int a, b, c;
    priority_queue<int> pq;
    cin >> x >> y >> z;
    pq.push(x);
    pq.push(y);
    pq.push(z);
    c = pq.top();
    pq.pop();
    b = pq.top();
    pq.pop();
    a = pq.top();
    pq.pop();

    string order;
    cin >> order;

    for (int i = 0; i < 3; i++){
        char letter = tolower(order[i]);
        if (letter == 'a'){
            cout << a;
        }
        else if (letter == 'b'){
            cout << b;
        }
        else if (letter == 'c'){
            cout << c;
        }
        if (i != 2){
            cout << ' ';
        }
    }
    return 0;
}
