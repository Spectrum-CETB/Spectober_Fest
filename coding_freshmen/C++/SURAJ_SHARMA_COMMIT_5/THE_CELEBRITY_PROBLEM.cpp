
class Solution 
{
    private:
    bool knows(int a,int b,vector<vector<int> >& M){
        if(M[a][b]==1){
            return true;
        }
        else{
            return false;
        }
    }
    int verify(int ans,vector<vector<int> >& M,int n){
        int zerocount=0;
        for(int i=0;i<n;i++){
            if(M[ans][i]==0){
                zerocount++;
            }
        }
        int onecount=0;
        for(int i=0;i<n;i++){
            if(M[i][ans]==1){
                onecount++;
            }
            
        }
        if((zerocount==n)&&(onecount==n-1)){
            return ans;
        }
        else{
            return -1;
        }
    }
    public:
    //Function to find if there is a celebrity in the party or not.
    int celebrity(vector<vector<int> >& M, int n) 
    {
        // code here
        stack<int> s;
        for(int i=0;i<n;i++){
            s.push(i);
        }
        while(s.size()>1){
            int a=s.top();
            s.pop();
            int b=s.top();
            s.pop();
            if(knows(a,b,M)){
                s.push(b);
            }
            else{
                s.push(a);
            }
        
        }
        int ans=s.top();
        if(verify(ans,M,n)!=-1){
            return verify(ans,M,n);
        }
        else{
            return -1;
        }
    }
};