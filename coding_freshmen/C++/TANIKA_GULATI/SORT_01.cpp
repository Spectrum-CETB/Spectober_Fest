#include <bits/stdc++.h>
using namespace std;

int main()
{
    int length;
    cout << "Enter length of array: ";
    cin >> length;
    int array[length];
    for (int i = 0; i < length; i++)
    {
        cin >> array[i];
    }
    int start = 0;
    int end = length - 1;
    while (start < end)
    {
        if (array[start] == 1)
        {
            swap(array[start], array[end]);
            end--;
        }
        else
            start++;
    }
    for (int i = 0; i < length; i++)
        cout << array[i] << " ";
}
