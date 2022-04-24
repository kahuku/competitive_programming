#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int nM, nG;
        cin >> nG >> nM;
        vector<int> mA, gA;
        for (int j = 0; j < nG; j++){
            int num;
            cin >> num;
            gA.push_back(num);
        }
        for (int j = 0; j < nM; j++){
            int num;
            cin >> num;
            mA.push_back(num);
        }
        sort(mA.begin(), mA.end());
        sort(gA.begin(), gA.end());
        while (mA.size() != 0 && gA.size() != 0){
            if (mA[0] > gA[0]){
                gA.erase(gA.begin());
            }
            else {
                mA.erase(mA.begin());
            }
        }
        /*
        for (int l = 0; l < mA.size(); l++){
            cout << "mA[" << l << "] = " << mA[l] << endl;
        }
        for (int l = 0; l < gA.size(); l++){
            cout << "gA[" << l << "] = " << gA[l] << endl;
        }*/
        if (gA.size() == 0){
            cout << "MechaGodzilla" << endl;
        }
        else if (mA.size() == 0){
            cout << "Godzilla" << endl;
        }
        else{
            cout << "uncertain" << endl;
        }
    }
    return 0;
}
