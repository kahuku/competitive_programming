#include <iostream>
using namespace std;
int main() {
    int contestants[5];

    for (int i = 0; i < 5; i++){
        int sum = 0;
        for (int j = 0; j < 4; j++){
            int score;
            cin >> score;
            sum += score;
        }
        contestants[i] = sum;
    }

    int max = 0;
    for (int i = 0; i < 5; i++) {
        if (contestants[i] > contestants[max]){
            max = i;
        }
    }
    cout << max + 1 << " " << contestants[max] << endl;
    return 0;
}
