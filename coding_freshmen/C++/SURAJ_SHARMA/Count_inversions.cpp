class Solution{
  public:
    // arr[]: Input Array
    // N : Size of the Array arr[]
    
    // Function to count inversions in the array.
    
    long long int mergethem(long long *arr,long long s,long e){
   long long int i=s;
   long long int mid=(s+e)/2;
   long long int j=mid+1;
   long long int b[e+1];
   long long int mi=s;
   long long ans=0;
   while(i<=mid&&j<=e){
       if(arr[i]<=arr[j]){
           b[mi]=arr[i];
           i++;
           mi++;
          
           
       }
       else{
           b[mi]=arr[j];
           ans=ans+(mid-i+1);
           j++;
           mi++;
           
       }
   }
    
    while(i>mid&&j<=e){
        b[mi]=arr[j];
        j++;
        mi++;
        
        
    }
    while(i<=mid&&j>e){
        b[mi]=arr[i];
        i++;
        mi++;
        
        
    }
   // cout<<ans-1<<" "<<endl;
    for(int i=s;i<e+1;i++){
        arr[i]=b[i];
    }
  return ans;
}
long long int merge(long long *arr,long s,long long e){
    long long ans=0;
    
    if(s<e){
        
    int mid=(s+e)/2;
    ans=ans+merge(arr,s,mid);
    ans=ans+merge(arr,mid+1,e);
    ans=ans+mergethem(arr,s,e);
    }
   return ans;
}
 
    long long int inversionCount(long long arr[], long long N)
    {
        // Your Code Here 
        long long s=0;
   long long e=N-1;
   long long mid=(s+e)/2;
  
   long long int ans=merge(arr,s,e);
   //long long int ans=0;
   //
   return ans;
    }

};

//{ Driver Code Starts.

int main() {
    
    long long T;
    cin >> T;
    
    while(T--){
        long long N;
        cin >> N;
        
        long long A[N];
        for(long long i = 0;i<N;i++){
            cin >> A[i];
        }
        Solution obj;
        cout << obj.inversionCount(A,N) << endl;
    }
    
    return 0;
}