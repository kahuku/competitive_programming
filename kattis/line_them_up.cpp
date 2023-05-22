#include <iostream>
#include <set>
#include <string>
using namespace std;
int main() {
    int n;
    cin >> n;
    string names[n];
    set<string> people;
    for (int i = 0; i < n; i++){
        string input;
        cin >> input;
        names[i] = input;
        people.insert(input);
    }
    //cout << "increasing" << endl;
    bool increasing = true;
    int i = 0;
    for (set<string>::iterator it = people.begin(); it != people.end(); it++){
        if (*it == names[i]){
            //cout << "true" << endl;
        }
        else{
            increasing = false;
        }
        i++;
    }

    bool decreasing = true;
    //cout << "Decreasing" << endl;
    int j = 0;
    for (set<string>::reverse_iterator rit = people.rbegin(); rit != people.rend(); rit++){
        if (*rit == names[j]){
            //cout << "true" << endl;
        }
        else{
            decreasing = false;
        }
        j++;
    }
    if (increasing){
        cout << "INCREASING" << endl;
    }
    else if (decreasing){
        cout << "DECREASING" << endl;
    }
    else {
        cout << "NEITHER" << endl;
    }
    return 0;
}
