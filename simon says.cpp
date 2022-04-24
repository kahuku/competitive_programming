#include <iostream>
#include <string>
using namespace std;
int main() {
    int n;
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++){
        string line;
        getline(cin, line);
        int found = line.find("Simon says");
        if (found != string::npos){
            string out = line.substr(found + 11, line.length());
            cout << out << endl;
        }
    }

    return 0;
}
