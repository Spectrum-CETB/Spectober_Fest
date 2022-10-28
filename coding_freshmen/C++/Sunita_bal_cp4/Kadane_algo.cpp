    public:
    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    long long maxSubarraySum(int arr[], int n){
        int ans;
        int max=arr[0];
        for(int j=1;j<n;j++){
            if(arr[j]>max){
                max=arr[j];
            }
        }
         ans=max;
         int maxsum=0;
         int cursum=0;
         for(int i=0;i<n;i++){
             cursum=cursum+arr[i];
             if(cursum>maxsum){
                 maxsum=cursum;
             }
             if(cursum<0){
                 cursum=0;
             }
             
         }
         if(maxsum==0){
             maxsum=ans;
         }
         return maxsum;
    }
};