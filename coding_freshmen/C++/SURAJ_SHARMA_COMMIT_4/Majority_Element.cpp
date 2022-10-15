int majorityElement(int a[], int size)
{
     int major=size/2;
    int ansIndex=0;
    int count=1;
    int cunt=0;
    for(int i=1;i<size;i++){
     if(a[i]==a[ansIndex]){
         
        count++;
    }
    else{
        count--;
    }
    if(count==0){
        ansIndex=i;
        count=1;
    }
    }
    for(int i=0;i<size;i++){
        if(a[i]==a[ansIndex]){
            cunt++;
        }
    }
    if(cunt>major){
        return a[ansIndex];
    }
    return -1;
        
}