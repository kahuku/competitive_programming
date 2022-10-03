#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


int get_next_fib(vector<int> nums) {
    return nums.at(nums.size() - 1) + nums.at(nums.size() - 2);
}

// Complete the fib function below.
vector<int> fib(int n) {
    vector<int> r;
    
    for (int i = 0; i < n; i++) {
        if (i == 0 || i == 1) {
            r.push_back(1);
        }
        else {
            r.push_back(get_next_fib(r));
        }
    }
    
    return r;
}
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<int> res = fib(n);

    for (int i = 0; i < res.size(); i++) {
        fout << res[i];

        if (i != res.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
