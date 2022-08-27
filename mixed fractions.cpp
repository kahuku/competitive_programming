#include <iostream>
using namespace std;

int main() {
    int num;
    int den;
    cin >> num >> den;
    while (num != 0 and den != 0){
        int whole = num / den;
        int rem = num % den;
        cout << whole << " " << rem << " / " << den << endl;
        cin >> num >> den;
    }
    return 0;
}
