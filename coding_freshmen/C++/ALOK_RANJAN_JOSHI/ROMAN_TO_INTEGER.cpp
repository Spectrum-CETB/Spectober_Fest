#include <bits/stdc++.h>
using namespace std;

int main()
{
    string roman_no;
    cout << "Roman Number = ";
    cin >> roman_no;
    int number = 0;
    map<char, int> roman_value_int = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
    for (int i = 0; i < roman_no.length(); i++)
    {
        if (roman_value_int[roman_no[i + 1]] <= roman_value_int[roman_no[i]])
            number += roman_value_int[roman_no[i]];
        else
            number -= roman_value_int[roman_no[i]];
    }
    cout << number << endl;
    return 0;
}