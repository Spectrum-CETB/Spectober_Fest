    public:
    int kthElement(int arr1[], int arr2[], int n, int m, int k)
    {
        vector<int> ans;
        int i=0,j=0;
        while(i<n&&j<m){
            if(arr1[i]<arr2[j]){
                ans.push_back(arr1[i]);
                i++;
            }
            else
            if(arr1[i]>arr2[j]){
                ans.push_back(arr2[j]);
                j++;
            }
            else
            if(arr1[i]==arr2[j]){
                 ans.push_back(arr2[j]);
                 ans.push_back(arr1[i]);
                 i++;
                 j++;
            }
        }
        while(i<n){
            ans.push_back(arr1[i]);
            i++;
        }
        while(j<m){
            ans.push_back(arr2[j]);
            j++;
        }
        int answr=ans[k-1];
        return answr;
    }
};