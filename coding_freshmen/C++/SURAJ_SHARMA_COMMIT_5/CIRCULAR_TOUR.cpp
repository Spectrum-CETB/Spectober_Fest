The structure of petrolPump is 
struct petrolPump
{
    int petrol;
    int distance;
};*/

/*You are required to complete this method*/
class Solution{
  public:
  
    //Function to find starting point where the truck can start to get through
    //the complete circle without exhausting its petrol in between.
    int tour(petrolPump p[],int n)
    {
       //Your code here
       int deficit=0;
       int balance=0;
       int start=0;
       for(int i=0;i<n;i++){
           balance+=p[i].petrol-p[i].distance;
           if(balance<0){
               deficit=deficit+balance;
               start=i+1;
               balance=0;
           }
       }
       if(deficit+balance>=0)
       return start;
       else{
           return -1;
       }
    }
};
