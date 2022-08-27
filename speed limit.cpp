#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    while (n != -1){
        int speed[n];
        int time[n];
        for (int i = 0; i < n; i++){
            cin >> speed[i];
            cin >> time[i];
        }
        int total = speed[0] * time[0];
        for (int i = 1; i < n; i++){
            total += speed[i] * (time[i] - time[i - 1]);
        }
        cout << total << " miles" << endl;
        cin >> n;
    }
    return 0;
}
