#include <iostream>
using namespace std;
int main() {
    int n, t;
    cin >> n >> t;
    int sum = 0;
    int count = 0;
    for (int i = 0; i < n; i++){
        int task_time;
        cin >> task_time;
        if (sum + task_time <= t){
            sum += task_time;
            count++;
        }
        else {
            cout << count << endl;
            return 0;
        }
    }
    cout << count << endl;
    return 0;
}
