#include <iostream>
using namespace std;
int main() {
    int s_hours, s_minutes;
    cin >> s_hours >> s_minutes;
    const int wake_time = 45;
    int tot_time = 60 * s_hours + s_minutes;
    tot_time -= wake_time;
    if (tot_time < 0){
        tot_time += 23 * 60 + 60;
    }
    int f_hours, f_minutes;
    f_hours = tot_time / 60;
    f_minutes = tot_time % 60;

    cout << f_hours << ' ' << f_minutes << endl;
    return 0;
}
