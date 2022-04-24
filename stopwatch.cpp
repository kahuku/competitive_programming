#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    if (n % 2 == 1) {
        cout << "Still running" << endl;
    }
    else{
        int arr[n];
        for (int i = 0; i < n; i++){
            cin >> arr[i];
        }
        int out = 0;
        for (int i = 0; i < n; i+=2){
            int num1 = arr[i];
            int num2 = arr[i+1];
            out += num2 - num1;
        }
        cout << out << endl;
    }
    return 0;
}
