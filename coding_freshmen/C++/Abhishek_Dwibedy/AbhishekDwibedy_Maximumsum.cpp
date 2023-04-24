#include <bits/stdc++.h>
using namespace std;

int maxSubArraySum(int arr[], int size)
{
	int maximum = INT_MIN, ending = 0,
		start = 0, end = 0, s = 0;

	for (int i = 0; i < size; i++) {
		ending += arr[i];

		if (maximum < ending) {
			maximum = ending;
			start = s;
			end = i;
		}

		if (ending < 0) {
			ending = 0;
			s = i + 1;
		}
	}
    return maximum;
}

/*Driver program to test maxSubArraySum*/
int main()
{
    int size;
    cin>>size;
    int array[size];
    for (int i = 0; i < size; i++)
    {
        cin>>array[i];
    }
	int max_sum = maxSubArraySum(array, size);
    cout<<max_sum;
	return 0;
}
