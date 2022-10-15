
class Solution{
    public:
    // arr[] : int input array of integers
    // k : the quadruple sum required
   vector<vector<int> > fourSum(vector<int> &nums, int target) {
       // Your code goes here
        vector<vector<int>>res;
       int n=nums.size();
       sort(nums.begin(),nums.end());
       for(int i=0;i<nums.size();i++)
       {
           for(int j=i+1;j<nums.size();j++)
           {
               int target2=target-(nums[i]+nums[j]);
               int front=j+1;
               int end=n-1;
               while(front<end)
               {
                   int twosum=nums[front]+nums[end];
                   if(twosum>target2)
                   {
                       end--;
                   }
                   else if(twosum<target2)
                   {
                       front++;
                   }
                   else
                   {
                       vector<int>quad(4,0);
                       quad[0]=nums[i];
                       quad[1]=nums[j];
                       quad[2]=nums[front];
                       quad[3]=nums[end];
                       res.push_back(quad);
                       while(front<end&&nums[front]==quad[2])
                       {
                           front++;
                       }
                       while(front<end&&nums[end]==quad[3])
                       {
                           end--;
                       }
                       
                   }
                   
                       
                   }
                   while(j+1<n&&nums[j+1]==nums[j])
                       {
                           j++;
                       }
               }
                 while(i+1<n&&nums[i+1]==nums[i])
                       {
                           i++;
                       }
           }
       return res;
       
   }
};