
class Solution
{
    int isPainter(int arr[],long long mid, int n, int k){
        long long painter = 1;
       long long boards = 0;
       for(int i=0; i<n; i++){
           if(boards+arr[i] <= mid){
               boards += arr[i];
           }
           else{
               painter++;
               if(painter>k || arr[i] > mid){
                   return false;
               }
               boards = arr[i];
           }
       }
       return true;
    }
  public:
    long long minTime(int arr[], int n, int k)
    {
        
        long long s=0;
        long long sum=0;
        
        for(int i=0; i<n; i++){
            sum += arr[i];
        }
        
        long long  e=sum;
        long long mid = s+(e-s)/2;
        long long ans=-1;
        
        while(s<=e){
            if(isPainter(arr,mid,n,k)){
                ans=mid;
                e=mid-1;
            }
            else{
                s=mid+1;
            }
            mid = s+(e-s)/2;
        }
        return ans;
    }
};